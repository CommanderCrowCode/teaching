#!/usr/bin/env python3
"""
Simple script to create Google Docs in the target folder
for the AI for Admins workshop.
"""

import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# The target folder ID for all workshop materials
TARGET_FOLDER_ID = "1oDG_0QykkSHVLUgoZREuxihzGYWPb-Sj"

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

# Directories containing the content files
DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
GOOGLE_DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'google_docs')
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

def create_document(docs_service, drive_service, title, content, folder_id):
    """Create a new Google Doc in the target folder."""
    # Create the document
    document_body = {
        'title': title
    }
    doc = docs_service.documents().create(body=document_body).execute()
    doc_id = doc.get('documentId')
    
    # Move the document to the target folder
    move_file_to_folder(drive_service, doc_id, folder_id)

    # Insert the content as plain text
    if content:
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={
                'requests': [
                    {
                        'insertText': {
                            'location': {
                                'index': 1
                            },
                            'text': content
                        }
                    }
                ]
            }
        ).execute()
    
    print(f"Created document '{title}' with ID: {doc_id} in target folder")
    return doc_id

def move_file_to_folder(drive_service, file_id, folder_id):
    """Move a file to the specified folder."""
    # Get the file's current parents
    file = drive_service.files().get(fileId=file_id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents', []))
    
    # Move the file to the new folder
    drive_service.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields='id, parents'
    ).execute()
    
    print(f"Moved file {file_id} to folder {folder_id}")

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
    
    # Lists to store document links
    google_docs_links = []
    ai_cases_links = []
    
    # Process Google Docs markdown files
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
            doc_id = create_document(docs_service, drive_service, md_file["title"], content, TARGET_FOLDER_ID)
            update_permission(drive_service, doc_id)
            google_docs_links.append({
                "title": md_file["title"],
                "link": f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
            })
    
    # Process AI Cases markdown files
    ai_files = [
        {"file": "effective_prompts_guide.md", "title": "Effective Prompts Guide - AI for Admins Workshop"},
        {"file": "document_creation_examples.md", "title": "Document Creation Examples - AI for Admins Workshop"},
        {"file": "data_analysis_examples.md", "title": "Data Analysis Examples - AI for Admins Workshop"},
        {"file": "email_response_examples.md", "title": "Email Response Examples - AI for Admins Workshop"},
        {"file": "university_prompts_collection.md", "title": "University Prompts Collection - AI for Admins Workshop"},
        {"file": "hands_on_exercises.md", "title": "Hands-on Exercises - AI for Admins Workshop"},
        {"file": "ai_integration_workflows.md", "title": "AI Integration Workflows - AI for Admins Workshop"},
    ]
    
    for ai_file in ai_files:
        file_path = os.path.join(AI_CASES_DIR, ai_file["file"])
        content = read_file_content(file_path)
        
        if content:
            doc_id = create_document(docs_service, drive_service, ai_file["title"], content, TARGET_FOLDER_ID)
            update_permission(drive_service, doc_id)
            ai_cases_links.append({
                "title": ai_file["title"],
                "link": f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
            })
    
    # Print and save all links
    print("\nGoogle Docs Links:")
    for doc in google_docs_links:
        print(f"{doc['title']}: {doc['link']}")
    
    print("\nAI Cases Links:")
    for doc in ai_cases_links:
        print(f"{doc['title']}: {doc['link']}")
    
    # Save the links to files for reference
    with open(os.path.join(GOOGLE_DOCS_DIR, "document_links.md"), "w") as f:
        f.write("# Google Docs Links for Workshop\n\n")
        for doc in google_docs_links:
            f.write(f"## {doc['title']}\n")
            f.write(f"[{doc['title']}]({doc['link']})\n\n")
    
    with open(os.path.join(AI_CASES_DIR, "document_links.md"), "w") as f:
        f.write("# Google Docs Links for AI Cases\n\n")
        for doc in ai_cases_links:
            f.write(f"## {doc['title']}\n")
            f.write(f"[{doc['title']}]({doc['link']})\n\n")
    
    # Save a combined links file in the root examples directory
    all_links = google_docs_links + ai_cases_links
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "all_document_links.md"), "w") as f:
        f.write("# All Google Docs Links for AI for Admins Workshop\n\n")
        f.write("## Google Docs Section\n\n")
        for doc in google_docs_links:
            f.write(f"- [{doc['title']}]({doc['link']})\n")
        
        f.write("\n## AI Cases Section\n\n")
        for doc in ai_cases_links:
            f.write(f"- [{doc['title']}]({doc['link']})\n")

if __name__ == "__main__":
    main()