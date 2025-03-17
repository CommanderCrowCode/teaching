#!/usr/bin/env python3
"""
Script to delete all DOCX files from the target Google Drive folder,
keeping only the converted Google Docs.
"""

import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# The target folder ID for all workshop materials
TARGET_FOLDER_ID = "1oDG_0QykkSHVLUgoZREuxihzGYWPb-Sj"

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    """Get valid credentials for Google Drive API."""
    creds = None
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'token.json')
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'credentials.json')
    
    # Try to use existing token
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_info(
            info=eval(open(token_path).read()), scopes=SCOPES)
    
    # If no valid credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def list_docx_files_in_folder(drive_service, folder_id):
    """List all DOCX files in the specified folder."""
    query = f"'{folder_id}' in parents and name contains '(DOCX)' and trashed = false"
    
    try:
        files = []
        page_token = None
        
        while True:
            response = drive_service.files().list(
                q=query,
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageToken=page_token
            ).execute()
            
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken')
            
            if not page_token:
                break
        
        return files
    except Exception as e:
        print(f"Error listing DOCX files: {str(e)}")
        return []

def delete_file(drive_service, file_id, file_name):
    """Delete a file from Google Drive."""
    try:
        drive_service.files().delete(fileId=file_id).execute()
        print(f"Deleted file: {file_name} (ID: {file_id})")
        return True
    except Exception as e:
        print(f"Error deleting file {file_name}: {str(e)}")
        return False

def main():
    """Main function to delete all DOCX files from the target folder."""
    
    # Get credentials
    creds = get_credentials()
    
    # Try to build and use the service
    try:
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        print(f"⚠️ ERROR: {str(e)}")
        return
    
    # List all DOCX files in the target folder
    docx_files = list_docx_files_in_folder(drive_service, TARGET_FOLDER_ID)
    
    if not docx_files:
        print("No DOCX files found in the target folder.")
        return
    
    print(f"Found {len(docx_files)} DOCX files in the target folder:")
    for file in docx_files:
        print(f"- {file['name']} (ID: {file['id']})")
    
    # Delete all DOCX files
    deleted_count = 0
    for file in docx_files:
        if delete_file(drive_service, file['id'], file['name']):
            deleted_count += 1
    
    print(f"\nDeleted {deleted_count} of {len(docx_files)} DOCX files from the target folder.")

if __name__ == "__main__":
    main()