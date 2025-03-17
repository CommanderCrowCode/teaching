#!/usr/bin/env python3
"""
Script to convert markdown to DOCX using pandoc, upload to Google Drive,
and convert to Google Docs format.
"""

import os
import json
import tempfile
import subprocess
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

# The target folder ID for all workshop materials
TARGET_FOLDER_ID = "1oDG_0QykkSHVLUgoZREuxihzGYWPb-Sj"

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    """Get valid credentials for Google Drive API."""
    creds = None
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'token.json')
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'credentials.json')
    
    # Always start fresh to avoid token scope issues
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())
    
    return creds

def convert_md_to_docx(md_file_path, output_docx_path):
    """Convert Markdown to DOCX using Pandoc."""
    try:
        # Use pandoc to convert markdown to DOCX
        cmd = ['pandoc', md_file_path, '-o', output_docx_path, '--reference-doc=reference.docx']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error converting {md_file_path} to DOCX: {result.stderr}")
            # Fallback to basic conversion without reference doc
            cmd = ['pandoc', md_file_path, '-o', output_docx_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"Error in fallback conversion: {result.stderr}")
                return False
        
        print(f"Successfully converted {md_file_path} to DOCX at {output_docx_path}")
        return True
    except Exception as e:
        print(f"Exception during pandoc conversion: {str(e)}")
        return False

def upload_file_to_drive(drive_service, file_path, file_name, mime_type, folder_id):
    """Upload a file to Google Drive in the specified folder."""
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    
    media = MediaFileUpload(
        file_path,
        mimetype=mime_type,
        resumable=True
    )
    
    try:
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f"Uploaded file {file_name} with ID: {file.get('id')}")
        return file.get('id')
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return None

def convert_to_google_docs(drive_service, file_id, title):
    """Convert an uploaded file to Google Docs format."""
    try:
        # Export the file as Google Docs
        # The Drive v3 API converts to Google Docs automatically when the file is uploaded
        # with the convert=True parameter, but we can also do it by copying the file
        # and specifying the Google Docs MIME type
        copied_file = drive_service.files().copy(
            fileId=file_id,
            body={
                'name': title,
                'mimeType': 'application/vnd.google-apps.document'
            }
        ).execute()
        
        print(f"Converted file to Google Docs with ID: {copied_file.get('id')}")
        return copied_file.get('id')
    except Exception as e:
        print(f"Error converting to Google Docs: {str(e)}")
        return None

def update_permission(drive_service, file_id):
    """Update the document permission to make it viewable by anyone with the link."""
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    
    try:
        drive_service.permissions().create(
            fileId=file_id,
            body=permission
        ).execute()
        print(f"Updated permissions for document with ID: {file_id}")
        return True
    except Exception as e:
        print(f"Error updating permissions: {str(e)}")
        return False

def process_markdown_file(drive_service, md_file_path, title):
    """Process a single markdown file - convert to DOCX, upload, and convert to Google Docs."""
    # Create a temporary DOCX file
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as temp_file:
        docx_path = temp_file.name
    
    try:
        # Convert markdown to DOCX
        if not convert_md_to_docx(md_file_path, docx_path):
            os.unlink(docx_path)
            return None
        
        # Upload DOCX to Google Drive
        docx_id = upload_file_to_drive(
            drive_service, 
            docx_path, 
            f"{title} (DOCX)", 
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            TARGET_FOLDER_ID
        )
        
        if not docx_id:
            os.unlink(docx_path)
            return None
        
        # Convert to Google Docs
        gdoc_id = convert_to_google_docs(drive_service, docx_id, title)
        
        if not gdoc_id:
            os.unlink(docx_path)
            return None
        
        # Update permissions
        update_permission(drive_service, gdoc_id)
        
        # Clean up the temporary file
        os.unlink(docx_path)
        
        return {
            "title": title,
            "docx_id": docx_id,
            "gdoc_id": gdoc_id,
            "link": f"https://docs.google.com/document/d/{gdoc_id}/edit?usp=sharing"
        }
    
    except Exception as e:
        print(f"Error processing file {md_file_path}: {str(e)}")
        if os.path.exists(docx_path):
            os.unlink(docx_path)
        return None

def main():
    """Main function to test with a single file."""
    
    # Get credentials
    creds = get_credentials()
    
    # Try to build and use the service
    try:
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        print(f"⚠️ ERROR: {str(e)}")
        return
    
    # Test with a single file - the Google Docs style guide
    test_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        'google_docs', 
        'style_guide.md'
    )
    
    test_title = "Google Docs Style Guide - AI for Admins Workshop"
    
    result = process_markdown_file(drive_service, test_file_path, test_title)
    
    if result:
        print("\nSuccessfully created Google Doc:")
        print(f"Title: {result['title']}")
        print(f"DOCX ID: {result['docx_id']}")
        print(f"Google Doc ID: {result['gdoc_id']}")
        print(f"Link: {result['link']}")
    else:
        print("\nFailed to create Google Doc")

if __name__ == "__main__":
    main()