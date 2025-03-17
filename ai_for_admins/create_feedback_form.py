#!/usr/bin/env python3
"""
Script to create a native Google Form in Thai for the AI for Admins workshop.
This script uses the Forms API directly to create the feedback form.
"""

import os
import json
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# The target folder ID for all workshop materials
TARGET_FOLDER_ID = "1oDG_0QykkSHVLUgoZREuxihzGYWPb-Sj"

# If modifying these scopes, delete the token.json file.
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/forms',
    'https://www.googleapis.com/auth/forms.body'
]

def get_credentials():
    """Get valid credentials for Google APIs."""
    creds = None
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'token.json')
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')
    
    # Always generate a fresh token with the right scopes
    if os.path.exists(token_path):
        try:
            os.remove(token_path)
            print("Removed existing token to ensure proper scopes.")
        except:
            pass
    
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())
    
    return creds

def create_google_form(creds, drive_service):
    """Create a Google Form using the Forms API directly."""
    
    access_token = creds.token
    
    # API endpoints
    forms_api_url = "https://forms.googleapis.com/v1/forms"
    batch_update_url = lambda form_id: f"https://forms.googleapis.com/v1/forms/{form_id}:batchUpdate"
    
    # Headers for the API requests
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    
    # Create the form - only set the title initially
    form_data = {
        "info": {
            "title": "แบบประเมินการอบรม: การใช้เครื่องมือดิจิทัลและ AI เพื่อเพิ่มประสิทธิภาพการทำงาน"
        }
    }
    
    # Create the form
    response = requests.post(forms_api_url, headers=headers, json=form_data)
    
    if response.status_code != 200:
        print(f"Error creating form: {response.status_code}")
        print(response.text)
        return None
    
    form_info = response.json()
    form_id = form_info.get("formId")
    
    print(f"Created form with ID: {form_id}")
    
    # Add description and questions to the form
    update_requests = {
        "requests": [
            # Add form description
            {
                "updateFormInfo": {
                    "info": {
                        "description": "แบบประเมินนี้ใช้เวลาประมาณ 5 นาทีในการกรอก ข้อมูลของท่านจะถูกเก็บเป็นความลับและนำไปใช้เพื่อการพัฒนาการอบรมในครั้งต่อไป"
                    },
                    "updateMask": "description"
                }
            },
            # Section 1: ข้อมูลทั่วไป
            {
                "createItem": {
                    "item": {
                        "title": "ข้อมูลทั่วไปของผู้เข้าร่วมอบรม",
                        "description": "กรุณาให้ข้อมูลเบื้องต้นเกี่ยวกับตัวท่าน",
                        "pageBreakItem": {}
                    },
                    "location": {"index": 0}
                }
            },
            # Q1: หน่วยงาน/คณะ
            {
                "createItem": {
                    "item": {
                        "title": "หน่วยงาน/คณะของท่าน",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": False
                                }
                            }
                        }
                    },
                    "location": {"index": 1}
                }
            },
            # Q2: ตำแหน่งงาน
            {
                "createItem": {
                    "item": {
                        "title": "ตำแหน่งงานของท่าน",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": False
                                }
                            }
                        }
                    },
                    "location": {"index": 2}
                }
            },
            # Q3: ประสบการณ์การใช้งาน AI
            {
                "createItem": {
                    "item": {
                        "title": "ประสบการณ์การใช้งาน AI ก่อนเข้าร่วมการอบรม",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": [
                                        {"value": "ไม่เคยใช้งานมาก่อน"},
                                        {"value": "เคยลองใช้งานบ้างเล็กน้อย"},
                                        {"value": "ใช้งานเป็นครั้งคราว"},
                                        {"value": "ใช้งานประจำ"}
                                    ]
                                }
                            }
                        }
                    },
                    "location": {"index": 3}
                }
            },
            
            # Section 2: การประเมินเนื้อหาการอบรม
            {
                "createItem": {
                    "item": {
                        "title": "การประเมินเนื้อหาการอบรม",
                        "description": "กรุณาประเมินเนื้อหาในแต่ละช่วงของการอบรม",
                        "pageBreakItem": {}
                    },
                    "location": {"index": 4}
                }
            },
            # Q4: ช่วงที่ 1: แนะนำเครื่องมือดิจิทัลและ AI
            {
                "createItem": {
                    "item": {
                        "title": "ช่วงที่ 1: แนะนำเครื่องมือดิจิทัลและ AI",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เป็นประโยชน์",
                                    "highLabel": "เป็นประโยชน์มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 5}
                }
            },
            # Q5: ช่วงที่ 2: หลักการ "Tidy Data"
            {
                "createItem": {
                    "item": {
                        "title": "ช่วงที่ 2: หลักการ \"Tidy Data\"",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เป็นประโยชน์",
                                    "highLabel": "เป็นประโยชน์มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 6}
                }
            },
            # Q6: ช่วงที่ 3: เริ่มต้นใช้งาน AI
            {
                "createItem": {
                    "item": {
                        "title": "ช่วงที่ 3: เริ่มต้นใช้งาน AI",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เป็นประโยชน์",
                                    "highLabel": "เป็นประโยชน์มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 7}
                }
            },
            # Q7: ช่วงที่ 4: การประยุกต์ใช้จริงในการทำงาน
            {
                "createItem": {
                    "item": {
                        "title": "ช่วงที่ 4: การประยุกต์ใช้จริงในการทำงาน",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เป็นประโยชน์",
                                    "highLabel": "เป็นประโยชน์มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 8}
                }
            },
            
            # Section 3: การประเมินวิทยากรและการจัดอบรม
            {
                "createItem": {
                    "item": {
                        "title": "การประเมินวิทยากรและการจัดอบรม",
                        "description": "กรุณาประเมินวิทยากรและการจัดอบรมโดยรวม",
                        "pageBreakItem": {}
                    },
                    "location": {"index": 9}
                }
            },
            # Q8: วิทยากรมีความรู้และทักษะในการถ่ายทอดความรู้
            {
                "createItem": {
                    "item": {
                        "title": "วิทยากรมีความรู้และทักษะในการถ่ายทอดความรู้",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "น้อย",
                                    "highLabel": "มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 10}
                }
            },
            # Q9: การอบรมมีความเหมาะสมกับระดับความรู้พื้นฐานของผู้เข้าร่วม
            {
                "createItem": {
                    "item": {
                        "title": "การอบรมมีความเหมาะสมกับระดับความรู้พื้นฐานของผู้เข้าร่วม",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เหมาะสม",
                                    "highLabel": "เหมาะสมมาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 11}
                }
            },
            # Q10: ระยะเวลาในการอบรมมีความเหมาะสม
            {
                "createItem": {
                    "item": {
                        "title": "ระยะเวลาในการอบรมมีความเหมาะสม",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "ไม่เหมาะสม",
                                    "highLabel": "เหมาะสมมาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 12}
                }
            },
            
            # Section 4: การนำไปใช้และข้อเสนอแนะ
            {
                "createItem": {
                    "item": {
                        "title": "การนำไปใช้และข้อเสนอแนะ",
                        "description": "กรุณาให้ข้อมูลเกี่ยวกับการนำความรู้ไปใช้และข้อเสนอแนะเพิ่มเติม",
                        "pageBreakItem": {}
                    },
                    "location": {"index": 13}
                }
            },
            # Q11: ท่านคิดว่าจะนำความรู้ที่ได้ไปประยุกต์ใช้ในงานของท่านอย่างไร
            {
                "createItem": {
                    "item": {
                        "title": "ท่านคิดว่าจะนำความรู้ที่ได้ไปประยุกต์ใช้ในงานของท่านอย่างไร",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {
                                    "paragraph": True
                                }
                            }
                        }
                    },
                    "location": {"index": 14}
                }
            },
            # Q12: เนื้อหาใดที่ท่านต้องการเรียนรู้เพิ่มเติม
            {
                "createItem": {
                    "item": {
                        "title": "เนื้อหาใดที่ท่านต้องการเรียนรู้เพิ่มเติม",
                        "questionItem": {
                            "question": {
                                "required": False,
                                "textQuestion": {
                                    "paragraph": True
                                }
                            }
                        }
                    },
                    "location": {"index": 15}
                }
            },
            # Q13: ข้อเสนอแนะอื่นๆ เพื่อปรับปรุงการอบรมในครั้งต่อไป
            {
                "createItem": {
                    "item": {
                        "title": "ข้อเสนอแนะอื่นๆ เพื่อปรับปรุงการอบรมในครั้งต่อไป",
                        "questionItem": {
                            "question": {
                                "required": False,
                                "textQuestion": {
                                    "paragraph": True
                                }
                            }
                        }
                    },
                    "location": {"index": 16}
                }
            },
            # Q14: ความพึงพอใจโดยรวมต่อการอบรมครั้งนี้
            {
                "createItem": {
                    "item": {
                        "title": "ความพึงพอใจโดยรวมต่อการอบรมครั้งนี้",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "scaleQuestion": {
                                    "low": 1,
                                    "high": 5,
                                    "lowLabel": "น้อย",
                                    "highLabel": "มาก"
                                }
                            }
                        }
                    },
                    "location": {"index": 17}
                }
            }
        ]
    }
    
    # Add questions to the form
    update_response = requests.post(
        batch_update_url(form_id),
        headers=headers,
        json=update_requests
    )
    
    if update_response.status_code != 200:
        print(f"Error adding questions to form: {update_response.status_code}")
        print(update_response.text)
        return None
    
    # Move the form to the target folder
    try:
        move_file_to_folder(drive_service, form_id, TARGET_FOLDER_ID)
    except Exception as e:
        print(f"Warning: Could not move form to target folder: {str(e)}")
    
    # Get the form URL
    form_url = f"https://docs.google.com/forms/d/{form_id}/edit"
    response_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
    
    return {
        "form_id": form_id,
        "edit_url": form_url,
        "response_url": response_url
    }

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
    
    print(f"Moved form {file_id} to folder {folder_id}")

def main():
    """Main function to create Google Form for feedback."""
    
    # Get credentials
    creds = get_credentials()
    
    # Try to build and use the service
    try:
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        print(f"⚠️ ERROR: {str(e)}")
        return
    
    # Create the feedback form
    result = create_google_form(creds, drive_service)
    
    if not result:
        print("Failed to create feedback form.")
        return
    
    # Print the form URLs
    print("\nแบบประเมินการอบรม AI สำหรับบุคลากรมหาวิทยาลัย ได้ถูกสร้างเรียบร้อยแล้ว:")
    print(f"URL สำหรับแก้ไขแบบฟอร์ม: {result['edit_url']}")
    print(f"URL สำหรับตอบแบบฟอร์ม: {result['response_url']}")
    
    # Save the form URLs to a file for reference
    with open("feedback_form_links.md", "w") as f:
        f.write("# แบบประเมินการอบรม AI สำหรับบุคลากรมหาวิทยาลัย\n\n")
        f.write(f"## URL สำหรับตอบแบบฟอร์ม\n")
        f.write(f"[แบบประเมินการอบรม]({result['response_url']})\n\n")
        f.write(f"## URL สำหรับแก้ไขแบบฟอร์ม\n")
        f.write(f"[แก้ไขแบบฟอร์ม]({result['edit_url']})\n\n")

if __name__ == "__main__":
    main()