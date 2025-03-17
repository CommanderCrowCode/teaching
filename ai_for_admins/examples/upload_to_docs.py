#!/usr/bin/env python3
"""
Script to create Google Docs for AI for Admins workshop.
Requires the Google API client library and credentials.json file.
"""

import os
import re
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

# Try to use the same token file as the sheets script
# If the script fails, manually delete the token.json file and try again

# Directories containing the content files
DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
GOOGLE_DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'google_docs')

def get_credentials():
    """Get valid credentials for Google Docs API."""
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

def create_document(service, title, content):
    """Create a new Google Doc with title and markdown content."""
    document_body = {
        'title': title
    }
    doc = service.documents().create(body=document_body).execute()
    doc_id = doc.get('documentId')
    
    # Convert markdown to simple content for Google Docs
    requests = convert_content_to_requests(content)
    
    if requests:
        # Insert the content into the document
        service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': requests}
        ).execute()
    
    print(f"Created document '{title}' with ID: {doc_id}")
    return doc_id

def convert_content_to_requests(content):
    """Convert markdown-like content to Google Docs API requests."""
    # Simple conversion for demonstration purposes
    requests = []
    
    # Replace HTML tags with appropriate text
    content = re.sub(r'<[^>]*>', '', content)
    
    # Insert the content at the start of the document
    requests.append({
        'insertText': {
            'location': {
                'index': 1
            },
            'text': content
        }
    })
    
    return requests

def read_file_content(file_path):
    """Read content from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def update_permission(drive_service, file_id):
    """Update the document permission to make it viewable by anyone with the link."""
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    drive_service.permissions().create(
        fileId=file_id,
        body=permission
    ).execute()
    print(f"Updated permissions for document with ID: {file_id}")

def check_api_enabled(service_name, project_id):
    """Print helpful message if the API is not enabled."""
    console_url = f"https://console.developers.google.com/apis/api/{service_name}/overview?project={project_id}"
    print(f"\n⚠️  ERROR: The {service_name} API is not enabled for this project.")
    print(f"Please enable it by visiting:\n{console_url}")
    print("\nAfter enabling the API, wait a few minutes for the changes to propagate, then run this script again.")
    return False

def process_html_file(file_path):
    """Extract content from HTML file, simplified for demonstration."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove HTML and body tags but keep other tags for formatting conversion
            content = re.sub(r'<!DOCTYPE[^>]*>', '', content)
            content = re.sub(r'<html[^>]*>(.*?)</html>', r'\1', content, flags=re.DOTALL)
            content = re.sub(r'<head>.*?</head>', '', content, flags=re.DOTALL)
            content = re.sub(r'<body[^>]*>(.*?)</body>', r'\1', content, flags=re.DOTALL)
            return content
    except Exception as e:
        print(f"Error processing HTML file {file_path}: {e}")
        return None

def main():
    """Main function to create Google Docs for the workshop."""
    # Extract project ID from credentials.json
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'credentials.json')
    with open(credentials_path, 'r') as f:
        creds_data = json.load(f)
        project_id = creds_data.get('installed', {}).get('project_id', 'unknown')
    
    # Get credentials
    creds = get_credentials()
    
    # Try to build and use the service
    try:
        docs_service = build('docs', 'v1', credentials=creds)
        
        # Test if Docs API is enabled by making a simple request
        try:
            docs_service.documents().get(documentId="1").execute()
        except Exception as e:
            error_str = str(e)
            if "docs.googleapis.com" in error_str and ("disabled" in error_str or "has not been used" in error_str):
                check_api_enabled("docs.googleapis.com", project_id)
                return
            # Ignore 404 errors, which are expected for a non-existent document ID
            if "404" not in error_str:
                raise
        
        drive_service = build('drive', 'v3', credentials=creds)
        
        # Test if Drive API is enabled
        try:
            drive_service.files().list(pageSize=1).execute() 
        except Exception as e:
            error_str = str(e)
            if "drive.googleapis.com" in error_str and ("disabled" in error_str or "has not been used" in error_str):
                check_api_enabled("drive.googleapis.com", project_id)
                return
            raise
    except Exception as e:
        print(f"⚠️ ERROR: {str(e)}")
        return
    
    # List to store document info
    doc_links = []
    
    # Process Markdown files from google_docs directory
    md_files = [
        {"file": "style_guide.md", "title": "Google Docs Style Guide - AI for Admins Workshop"},
        {"file": "templates_guide.md", "title": "Google Docs Templates Guide - AI for Admins Workshop"},
        {"file": "formatting_exercises.md", "title": "Google Docs Formatting Exercises - AI for Admins Workshop"},
        {"file": "collaboration_guide.md", "title": "Google Docs Collaboration Guide - AI for Admins Workshop"},
    ]
    
    for md_file in md_files:
        file_path = os.path.join(GOOGLE_DOCS_DIR, md_file["file"])
        content = read_file_content(file_path)
        
        if content:
            doc_id = create_document(docs_service, md_file["title"], content)
            update_permission(drive_service, doc_id)
            doc_links.append({
                "title": md_file["title"],
                "link": f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
            })
    
    # Process HTML files from docs directory
    html_files = [
        {"file": "university_style_guide.html", "title": "University Style Guide - AI for Admins Workshop"},
        {"file": "approval_form_template.html", "title": "Approval Form Template - AI for Admins Workshop"},
        {"file": "internal_memo_template.html", "title": "Internal Memo Template - AI for Admins Workshop"},
        {"file": "meeting_minutes_template.html", "title": "Meeting Minutes Template - AI for Admins Workshop"},
        {"file": "poorly_formatted_document.html", "title": "Poorly Formatted Document - AI for Admins Workshop"},
        {"file": "well_formatted_document.html", "title": "Well Formatted Document - AI for Admins Workshop"},
    ]
    
    for html_file in html_files:
        file_path = os.path.join(DOCS_DIR, html_file["file"])
        content = process_html_file(file_path)
        
        if content:
            doc_id = create_document(docs_service, html_file["title"], content)
            update_permission(drive_service, doc_id)
            doc_links.append({
                "title": html_file["title"],
                "link": f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
            })
    
    # Print and save the links
    print("\nGoogle Docs Links:")
    for doc in doc_links:
        print(f"{doc['title']}: {doc['link']}")
    
    # Save the links to a file for reference
    with open(os.path.join(GOOGLE_DOCS_DIR, "document_links.md"), "w") as f:
        f.write("# Google Docs Links for Workshop\n\n")
        for doc in doc_links:
            f.write(f"## {doc['title']}\n")
            f.write(f"[{doc['title']}]({doc['link']})\n\n")

if __name__ == "__main__":
    main()