#!/usr/bin/env python3
"""
Script to create Google Docs for AI Cases - AI for Admins workshop.
Requires the Google API client library and credentials.json file.
"""

import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

# Directory containing the content files
AI_CASES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ai_cases')

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
    
    # Insert the content into the document
    insert_text_request = [
        {
            'insertText': {
                'location': {
                    'index': 1
                },
                'text': content
            }
        }
    ]
    
    if insert_text_request:
        service.documents().batchUpdate(
            documentId=doc_id,
            body={'requests': insert_text_request}
        ).execute()
    
    print(f"Created document '{title}' with ID: {doc_id}")
    return doc_id

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

def main():
    """Main function to create Google Docs for the workshop."""
    
    # Get credentials
    creds = get_credentials()
    
    # Try to build and use the service
    try:
        docs_service = build('docs', 'v1', credentials=creds)
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        print(f"⚠️ ERROR: {str(e)}")
        return
    
    # List to store document info
    doc_links = []
    
    # Process Markdown files from AI cases directory
    md_files = [
        {"file": "effective_prompts_guide.md", "title": "Effective Prompts Guide - AI for Admins Workshop"},
        {"file": "document_creation_examples.md", "title": "Document Creation Examples - AI for Admins Workshop"},
        {"file": "data_analysis_examples.md", "title": "Data Analysis Examples - AI for Admins Workshop"},
        {"file": "email_response_examples.md", "title": "Email Response Examples - AI for Admins Workshop"},
        {"file": "university_prompts_collection.md", "title": "University Prompts Collection - AI for Admins Workshop"},
        {"file": "hands_on_exercises.md", "title": "Hands-on Exercises - AI for Admins Workshop"},
        {"file": "ai_integration_workflows.md", "title": "AI Integration Workflows - AI for Admins Workshop"},
    ]
    
    for md_file in md_files:
        file_path = os.path.join(AI_CASES_DIR, md_file["file"])
        content = read_file_content(file_path)
        
        if content:
            doc_id = create_document(docs_service, md_file["title"], content)
            update_permission(drive_service, doc_id)
            doc_links.append({
                "title": md_file["title"],
                "link": f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
            })
    
    # Print and save the links
    print("\nGoogle Docs Links for AI Cases:")
    for doc in doc_links:
        print(f"{doc['title']}: {doc['link']}")
    
    # Save the links to a file for reference
    with open(os.path.join(AI_CASES_DIR, "document_links.md"), "w") as f:
        f.write("# Google Docs Links for AI Cases\n\n")
        for doc in doc_links:
            f.write(f"## {doc['title']}\n")
            f.write(f"[{doc['title']}]({doc['link']})\n\n")

if __name__ == "__main__":
    main()