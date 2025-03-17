#!/usr/bin/env python3
"""
Script to upload CSV examples to Google Sheets for AI for Admins workshop.
Requires the Google API client library and credentials.json file.
"""

import os
import csv
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Directory containing the CSV files
CSV_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sheets')

def get_credentials():
    """Get valid credentials for Google Sheets API."""
    creds = None
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'token.json')
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'credentials.json')
    
    # Token file stores the user's access and refresh tokens
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
            token.write(str(creds.to_json()))
    
    return creds

def create_spreadsheet(service, title):
    """Create a new Google Spreadsheet."""
    spreadsheet_body = {
        'properties': {
            'title': title
        }
    }
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    print(f"Created spreadsheet '{title}' with ID: {response['spreadsheetId']}")
    return response['spreadsheetId']

def update_permission(drive_service, file_id):
    """Update the spreadsheet permission to make it viewable by anyone with the link."""
    permission = {
        'type': 'anyone',
        'role': 'reader',
    }
    drive_service.permissions().create(
        fileId=file_id,
        body=permission
    ).execute()
    print(f"Updated permissions for spreadsheet with ID: {file_id}")

def csv_to_sheet(service, spreadsheet_id, sheet_name, csv_file):
    """Upload CSV data to a specified sheet in the spreadsheet."""
    # Read CSV data
    data = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    # Create a new sheet
    batch_update_body = {
        'requests': [
            {
                'addSheet': {
                    'properties': {
                        'title': sheet_name
                    }
                }
            }
        ]
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, 
        body=batch_update_body
    ).execute()
    
    # Prepare the update body
    update_body = {
        'values': data
    }
    
    # Update the sheet with CSV data
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!A1',
        valueInputOption='RAW',
        body=update_body
    ).execute()
    
    print(f"Uploaded data to sheet '{sheet_name}' in spreadsheet with ID: {spreadsheet_id}")

def check_api_enabled(service_name, project_id):
    """Print helpful message if the API is not enabled."""
    console_url = f"https://console.developers.google.com/apis/api/{service_name}/overview?project={project_id}"
    print(f"\n⚠️  ERROR: The {service_name} API is not enabled for this project.")
    print(f"Please enable it by visiting:\n{console_url}")
    print("\nAfter enabling the API, wait a few minutes for the changes to propagate, then run this script again.")
    return False

def main():
    """Main function to upload all CSV files to Google Sheets."""
    # Extract project ID from credentials.json
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'credentials.json')
    with open(credentials_path, 'r') as f:
        import json
        creds_data = json.load(f)
        project_id = creds_data.get('installed', {}).get('project_id', 'unknown')
    
    try:
        creds = get_credentials()
        sheets_service = build('sheets', 'v4', credentials=creds)
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        error_str = str(e)
        if "SERVICE_DISABLED" in error_str:
            if "sheets.googleapis.com" in error_str:
                check_api_enabled("sheets.googleapis.com", project_id)
            elif "drive.googleapis.com" in error_str:
                check_api_enabled("drive.googleapis.com", project_id)
            else:
                print(f"⚠️  ERROR: An API is disabled: {error_str}")
            return
    
    # Create a spreadsheet for student registration data
    student_reg_spreadsheet_id = create_spreadsheet(sheets_service, "Student Registration Data - AI for Admins Workshop")
    
    # Upload untidy and tidy student registration data
    csv_to_sheet(
        sheets_service, 
        student_reg_spreadsheet_id, 
        "Untidy Data", 
        os.path.join(CSV_DIR, "untidy_student_registration.csv")
    )
    
    csv_to_sheet(
        sheets_service, 
        student_reg_spreadsheet_id, 
        "Tidy Data", 
        os.path.join(CSV_DIR, "tidy_student_registration.csv")
    )
    
    # Create a spreadsheet for faculty projects data
    faculty_proj_spreadsheet_id = create_spreadsheet(sheets_service, "Faculty Projects Data - AI for Admins Workshop")
    
    # Upload untidy and tidy faculty projects data
    csv_to_sheet(
        sheets_service, 
        faculty_proj_spreadsheet_id, 
        "Untidy Data", 
        os.path.join(CSV_DIR, "untidy_faculty_projects.csv")
    )
    
    csv_to_sheet(
        sheets_service, 
        faculty_proj_spreadsheet_id, 
        "Tidy Data", 
        os.path.join(CSV_DIR, "tidy_faculty_projects.csv")
    )
    
    # Update permissions to make the spreadsheets viewable by anyone with the link
    update_permission(drive_service, student_reg_spreadsheet_id)
    update_permission(drive_service, faculty_proj_spreadsheet_id)
    
    # Get and print the links to the spreadsheets
    student_reg_link = f"https://docs.google.com/spreadsheets/d/{student_reg_spreadsheet_id}/edit?usp=sharing"
    faculty_proj_link = f"https://docs.google.com/spreadsheets/d/{faculty_proj_spreadsheet_id}/edit?usp=sharing"
    
    print("\nSpreadsheet Links:")
    print(f"Student Registration Data: {student_reg_link}")
    print(f"Faculty Projects Data: {faculty_proj_link}")
    
    # Save the links to a file for reference
    with open(os.path.join(CSV_DIR, "spreadsheet_links.md"), "w") as f:
        f.write("# Google Sheets Links for Workshop\n\n")
        f.write("## Student Registration Data\n")
        f.write(f"[Student Registration Data - AI for Admins Workshop]({student_reg_link})\n\n")
        f.write("## Faculty Projects Data\n")
        f.write(f"[Faculty Projects Data - AI for Admins Workshop]({faculty_proj_link})\n")

if __name__ == "__main__":
    main()