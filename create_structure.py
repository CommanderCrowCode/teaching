from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
import io
from googleapiclient.http import MediaIoBaseUpload
import logging

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("aun_qa_creation.log"),
        logging.StreamHandler()
    ]
)

def get_credentials():
    """Get and validate Google Drive credentials."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If credentials don't exist or are invalid, ask the user to log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return credsdef create_folder(service, folder_name, parent_folder_id=None):
    """Create a folder in Google Drive."""
    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    if parent_folder_id:
        folder_metadata['parents'] = [parent_folder_id]
    
    folder = service.files().create(body=folder_metadata, fields='id').execute()
    folder_id = folder.get('id')
    logging.info(f"Created folder: {folder_name} (ID: {folder_id})")
    return folder_id

def create_file(service, file_name, file_content, parent_folder_id=None):
    """Create a text file with placeholder content in Google Drive."""
    file_metadata = {
        'name': file_name
    }
    
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]
    
    # Determine the MIME type based on file extension
    mime_type = 'text/plain'  # Default
    if file_name.endswith('.docx'):
        mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    elif file_name.endswith('.xlsx'):
        mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif file_name.endswith('.pdf'):
        mime_type = 'application/pdf'
    elif file_name.endswith('.pptx'):
        mime_type = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    
    # Create a media upload object
    media = MediaIoBaseUpload(
        io.BytesIO(file_content.encode('utf-8')),
        mimetype=mime_type,
        resumable=True
    )
    
    # Create the file
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    file_id = file.get('id')
    logging.info(f"Created file: {file_name} (ID: {file_id})")
    return file_iddef setup_aun_qa_structure(service, parent_folder_id=None):
    """Set up the entire AUN-QA folder structure in Google Drive."""
    # Create main folder
    logging.info("Creating main AUN-QA Programme Management folder...")
    aun_qa_folder_id = create_folder(service, "AUN-QA Programme Management", parent_folder_id)
    
    # Create main sub-folders
    logging.info("Creating main sub-folders...")
    folder_structure = {
        "0_Programme_Overview": create_folder(service, "0_Programme_Overview", aun_qa_folder_id),
        "1_Expected_Learning_Outcomes": create_folder(service, "1_Expected_Learning_Outcomes", aun_qa_folder_id),
        "2_Programme_Structure_and_Content": create_folder(service, "2_Programme_Structure_and_Content", aun_qa_folder_id),
        "3_Teaching_and_Learning_Approach": create_folder(service, "3_Teaching_and_Learning_Approach", aun_qa_folder_id),
        "4_Student_Assessment": create_folder(service, "4_Student_Assessment", aun_qa_folder_id),
        "5_Academic_Staff": create_folder(service, "5_Academic_Staff", aun_qa_folder_id),
        "6_Student_Support_Services": create_folder(service, "6_Student_Support_Services", aun_qa_folder_id),
        "7_Facilities_and_Infrastructure": create_folder(service, "7_Facilities_and_Infrastructure", aun_qa_folder_id),
        "8_Output_and_Outcomes": create_folder(service, "8_Output_and_Outcomes", aun_qa_folder_id),
        "SAR_Reports": create_folder(service, "SAR_Reports", aun_qa_folder_id),
        "Quality_Improvement_Plans": create_folder(service, "Quality_Improvement_Plans", aun_qa_folder_id),
    }
    
    return folder_structure, aun_qa_folder_iddef setup_programme_overview(service, parent_folder_id):
    """Set up the 0_Programme_Overview section."""
    logging.info("Setting up 0_Programme_Overview section...")
    
    # Create Strategic_Plans subfolder
    strategic_plans_id = create_folder(service, "Strategic_Plans", parent_folder_id)
    
    # Create files in 0_Programme_Overview
    create_file(service, "Programme_Specifications.docx", "Placeholder for programme specifications", parent_folder_id)
    create_file(service, "Vision_Mission_Statements.docx", "Placeholder for vision and mission statements", parent_folder_id)
    create_file(service, "Organisational_Structure.pdf", "Placeholder for organisational structure", parent_folder_id)
    create_file(service, "Programme_History.docx", "Placeholder for programme history", parent_folder_id)
    
    # Create files in Strategic_Plans
    create_file(service, "Department_Strategic_Plan.pdf", "Placeholder for department strategic plan", strategic_plans_id)
    create_file(service, "Faculty_Strategic_Plan.pdf", "Placeholder for faculty strategic plan", strategic_plans_id)def setup_expected_learning_outcomes(service, parent_folder_id):
    """Set up the 1_Expected_Learning_Outcomes section."""
    logging.info("Setting up 1_Expected_Learning_Outcomes section...")
    
    # Create subfolders
    elo_development_id = create_folder(service, "ELO_Development", parent_folder_id)
    elo_communication_id = create_folder(service, "ELO_Communication", parent_folder_id)
    
    # Create files in ELO_Development
    create_file(service, "ELO_Formulation_Process.docx", "Placeholder for ELO formulation process", elo_development_id)
    create_file(service, "Learning_Taxonomy_References.pdf", "Placeholder for learning taxonomy references", elo_development_id)
    create_file(service, "Stakeholder_Input_Analysis.xlsx", "Placeholder for stakeholder input analysis", elo_development_id)
    
    # Create files in ELO_Communication
    create_file(service, "Student_Handbook_ELO_Section.pdf", "Placeholder for student handbook ELO section", elo_communication_id)
    create_file(service, "Website_ELO_Content.pdf", "Placeholder for website ELO content", elo_communication_id)
    create_file(service, "Faculty_ELO_Training.pptx", "Placeholder for faculty ELO training", elo_communication_id)
    
    # Create files in 1_Expected_Learning_Outcomes
    create_file(service, "Programme_Learning_Outcomes.docx", "Placeholder for programme learning outcomes", parent_folder_id)
    create_file(service, "Course_Learning_Outcomes.xlsx", "Placeholder for course learning outcomes", parent_folder_id)
    create_file(service, "Generic_vs_Specific_Outcomes.xlsx", "Placeholder for generic vs specific outcomes", parent_folder_id)
    create_file(service, "ELO_Achievement_Data.xlsx", "Placeholder for ELO achievement data", parent_folder_id)def setup_programme_structure(service, parent_folder_id):
    """Set up the 2_Programme_Structure_and_Content section."""
    logging.info("Setting up 2_Programme_Structure_and_Content section...")
    
    # Create subfolders
    curriculum_design_id = create_folder(service, "Curriculum_Design", parent_folder_id)
    course_specs_id = create_folder(service, "Course_Specifications", parent_folder_id)
    curriculum_review_id = create_folder(service, "Curriculum_Review", parent_folder_id)
    
    # Create files in Curriculum_Design
    create_file(service, "Curriculum_Map.xlsx", "Placeholder for curriculum map", curriculum_design_id)
    create_file(service, "Course_Sequencing_Logic.docx", "Placeholder for course sequencing logic", curriculum_design_id)
    create_file(service, "Specialisation_Options.pdf", "Placeholder for specialisation options", curriculum_design_id)
    
    # Create subfolders in Course_Specifications
    create_file(service, "Course_Spec_Template.docx", "Placeholder for course spec template", course_specs_id)
    year1_id = create_folder(service, "Year_1_Courses", course_specs_id)
    year2_id = create_folder(service, "Year_2_Courses", course_specs_id)
    year3_id = create_folder(service, "Year_3_Courses", course_specs_id)
    year4_id = create_folder(service, "Year_4_Courses", course_specs_id)
    
    # Create files in Curriculum_Review
    create_file(service, "Review_Process.docx", "Placeholder for review process", curriculum_review_id)
    create_file(service, "Curriculum_Committee_Minutes.docx", "Placeholder for curriculum committee minutes", curriculum_review_id)
    create_file(service, "Stakeholder_Feedback.xlsx", "Placeholder for stakeholder feedback", curriculum_review_id)
    create_file(service, "Industry_Advisory_Panel_Reports.pdf", "Placeholder for industry advisory panel reports", curriculum_review_id)
    
    # Create files in main folder
    create_file(service, "Programme_Brochure.pdf", "Placeholder for programme brochure", parent_folder_id)def setup_teaching_learning(service, parent_folder_id):
    """Set up the 3_Teaching_and_Learning_Approach section."""
    logging.info("Setting up 3_Teaching_and_Learning_Approach section...")
    
    # Create subfolders
    educational_philosophy_id = create_folder(service, "Educational_Philosophy", parent_folder_id)
    teaching_methods_id = create_folder(service, "Teaching_Methods", parent_folder_id)
    lifelong_learning_id = create_folder(service, "Lifelong_Learning", parent_folder_id)
    entrepreneurship_id = create_folder(service, "Entrepreneurship_Innovation", parent_folder_id)
    teaching_improvement_id = create_folder(service, "Teaching_Improvement", parent_folder_id)
    
    # Create files in Educational_Philosophy
    create_file(service, "Teaching_Philosophy_Statement.docx", "Placeholder for teaching philosophy statement", educational_philosophy_id)
    create_file(service, "Communication_Evidence.pdf", "Placeholder for communication evidence", educational_philosophy_id)
    
    # Create files in Teaching_Methods
    create_file(service, "Active_Learning_Approaches.docx", "Placeholder for active learning approaches", teaching_methods_id)
    create_file(service, "Student_Centered_Learning.pdf", "Placeholder for student-centered learning", teaching_methods_id)
    create_file(service, "Innovative_Teaching_Examples.docx", "Placeholder for innovative teaching examples", teaching_methods_id)
    
    # Create files in Lifelong_Learning
    create_file(service, "Critical_Thinking_Development.docx", "Placeholder for critical thinking development", lifelong_learning_id)
    create_file(service, "Information_Literacy_Activities.pdf", "Placeholder for information literacy activities", lifelong_learning_id)
    
    # Create files in Entrepreneurship_Innovation
    create_file(service, "Creative_Thinking_Activities.docx", "Placeholder for creative thinking activities", entrepreneurship_id)
    create_file(service, "Entrepreneurship_Projects.pdf", "Placeholder for entrepreneurship projects", entrepreneurship_id)
    
    # Create files in Teaching_Improvement
    create_file(service, "Industry_Relevance_Reviews.docx", "Placeholder for industry relevance reviews", teaching_improvement_id)
    create_file(service, "Teaching_Improvement_Plans.xlsx", "Placeholder for teaching improvement plans", teaching_improvement_id)
    create_file(service, "Student_Feedback_Analysis.xlsx", "Placeholder for student feedback analysis", teaching_improvement_id)def setup_student_assessment(service, parent_folder_id):
    """Set up the 4_Student_Assessment section."""
    logging.info("Setting up 4_Student_Assessment section...")
    
    # Create subfolders
    assessment_methods_id = create_folder(service, "Assessment_Methods", parent_folder_id)
    assessment_policies_id = create_folder(service, "Assessment_Policies", parent_folder_id)
    assessment_standards_id = create_folder(service, "Assessment_Standards", parent_folder_id)
    feedback_processes_id = create_folder(service, "Feedback_Processes", parent_folder_id)
    assessment_review_id = create_folder(service, "Assessment_Review", parent_folder_id)
    
    # Create files in Assessment_Methods
    create_file(service, "Assessment_Types_Overview.docx", "Placeholder for assessment types overview", assessment_methods_id)
    create_file(service, "Constructive_Alignment_Map.xlsx", "Placeholder for constructive alignment map", assessment_methods_id)
    create_file(service, "Assessment_Examples.pdf", "Placeholder for assessment examples", assessment_methods_id)
    
    # Create files in Assessment_Policies
    create_file(service, "Assessment_Guidelines.pdf", "Placeholder for assessment guidelines", assessment_policies_id)
    create_file(service, "Assessment_Appeals_Process.docx", "Placeholder for assessment appeals process", assessment_policies_id)
    create_file(service, "Academic_Integrity_Policy.pdf", "Placeholder for academic integrity policy", assessment_policies_id)
    
    # Create files in Assessment_Standards
    create_file(service, "Grading_Criteria.pdf", "Placeholder for grading criteria", assessment_standards_id)
    create_file(service, "Rubrics.xlsx", "Placeholder for rubrics", assessment_standards_id)
    create_file(service, "Progression_Requirements.docx", "Placeholder for progression requirements", assessment_standards_id)
    
    # Create files in Feedback_Processes
    create_file(service, "Feedback_Guidelines.docx", "Placeholder for feedback guidelines", feedback_processes_id)
    create_file(service, "Feedback_Samples.pdf", "Placeholder for feedback samples", feedback_processes_id)
    create_file(service, "Feedback_Timeline_Analysis.xlsx", "Placeholder for feedback timeline analysis", feedback_processes_id)
    
    # Create files in Assessment_Review
    create_file(service, "Assessment_Review_Process.docx", "Placeholder for assessment review process", assessment_review_id)
    create_file(service, "Improvement_Actions.xlsx", "Placeholder for improvement actions", assessment_review_id)
    create_file(service, "Industry_Alignment_Review.pdf", "Placeholder for industry alignment review", assessment_review_id)def setup_academic_staff(service, parent_folder_id):
    """Set up the 5_Academic_Staff section."""
    logging.info("Setting up 5_Academic_Staff section...")
    
    # Create subfolders
    staff_planning_id = create_folder(service, "Staff_Planning", parent_folder_id)
    workload_management_id = create_folder(service, "Workload_Management", parent_folder_id)
    competency_management_id = create_folder(service, "Competency_Management", parent_folder_id)
    promotion_merit_id = create_folder(service, "Promotion_Merit_System", parent_folder_id)
    staff_rights_id = create_folder(service, "Staff_Rights_Ethics", parent_folder_id)
    staff_development_id = create_folder(service, "Staff_Development", parent_folder_id)
    performance_management_id = create_folder(service, "Performance_Management", parent_folder_id)
    
    # Create files in Staff_Planning
    create_file(service, "Staff_Requirements_Analysis.xlsx", "Placeholder for staff requirements analysis", staff_planning_id)
    create_file(service, "Succession_Planning.docx", "Placeholder for succession planning", staff_planning_id)
    create_file(service, "Recruitment_Strategy.pdf", "Placeholder for recruitment strategy", staff_planning_id)
    
    # Create files in Workload_Management
    create_file(service, "Workload_Model.xlsx", "Placeholder for workload model", workload_management_id)
    create_file(service, "Workload_Monitoring_Data.xlsx", "Placeholder for workload monitoring data", workload_management_id)
    create_file(service, "Workload_Improvement_Actions.docx", "Placeholder for workload improvement actions", workload_management_id)
    
    # Create files in Competency_Management
    create_file(service, "Staff_Competency_Framework.docx", "Placeholder for staff competency framework", competency_management_id)
    create_file(service, "Competency_Evaluation_Process.pdf", "Placeholder for competency evaluation process", competency_management_id)
    create_file(service, "Communication_of_Competencies.pdf", "Placeholder for communication of competencies", competency_management_id)
    
    # Create files in Promotion_Merit_System
    create_file(service, "Promotion_Criteria.pdf", "Placeholder for promotion criteria", promotion_merit_id)
    create_file(service, "Merit_System_Guidelines.docx", "Placeholder for merit system guidelines", promotion_merit_id)
    create_file(service, "Promotion_Case_Studies.pdf", "Placeholder for promotion case studies", promotion_merit_id)
    
    # Create files in Staff_Rights_Ethics
    create_file(service, "Academic_Freedom_Policy.pdf", "Placeholder for academic freedom policy", staff_rights_id)
    create_file(service, "Professional_Ethics_Code.docx", "Placeholder for professional ethics code", staff_rights_id)
    create_file(service, "Faculty_Handbook_Rights_Section.pdf", "Placeholder for faculty handbook rights section", staff_rights_id)
    
    # Create files in Staff_Development
    create_file(service, "Training_Needs_Analysis.xlsx", "Placeholder for training needs analysis", staff_development_id)
    create_file(service, "Staff_Development_Plan.docx", "Placeholder for staff development plan", staff_development_id)
    create_file(service, "Training_Records.xlsx", "Placeholder for training records", staff_development_id)
    
    # Create files in Performance_Management
    create_file(service, "Performance_Assessment_System.docx", "Placeholder for performance assessment system", performance_management_id)
    create_file(service, "Reward_Recognition_Scheme.pdf", "Placeholder for reward recognition scheme", performance_management_id)
    create_file(service, "Teaching_Research_Quality_Metrics.xlsx", "Placeholder for teaching research quality metrics", performance_management_id)def setup_student_support(service, parent_folder_id):
    """Set up the 6_Student_Support_Services section."""
    logging.info("Setting up 6_Student_Support_Services section...")
    
    # Create subfolders
    student_intake_id = create_folder(service, "Student_Intake", parent_folder_id)
    support_planning_id = create_folder(service, "Support_Services_Planning", parent_folder_id)
    student_monitoring_id = create_folder(service, "Student_Monitoring", parent_folder_id)
    cocurricular_id = create_folder(service, "Co-curricular_Activities", parent_folder_id)
    support_staff_id = create_folder(service, "Support_Staff_Competences", parent_folder_id)
    service_evaluation_id = create_folder(service, "Service_Evaluation", parent_folder_id)
    
    # Create files in Student_Intake
    create_file(service, "Admission_Policy.pdf", "Placeholder for admission policy", student_intake_id)
    create_file(service, "Admission_Procedures.docx", "Placeholder for admission procedures", student_intake_id)
    create_file(service, "Communication_of_Admission_Info.pdf", "Placeholder for communication of admission info", student_intake_id)
    
    # Create files in Support_Services_Planning
    create_file(service, "Short_Term_Support_Plan.docx", "Placeholder for short-term support plan", support_planning_id)
    create_file(service, "Long_Term_Support_Plan.docx", "Placeholder for long-term support plan", support_planning_id)
    create_file(service, "Service_Quality_Indicators.xlsx", "Placeholder for service quality indicators", support_planning_id)
    
    # Create files in Student_Monitoring
    create_file(service, "Progress_Monitoring_System.docx", "Placeholder for progress monitoring system", student_monitoring_id)
    create_file(service, "Performance_Recording_Process.pdf", "Placeholder for performance recording process", student_monitoring_id)
    create_file(service, "Feedback_Corrective_Actions.xlsx", "Placeholder for feedback corrective actions", student_monitoring_id)
    
    # Create files in Co-curricular_Activities
    create_file(service, "Activity_Catalogue.docx", "Placeholder for activity catalogue", cocurricular_id)
    create_file(service, "Competition_Opportunities.pdf", "Placeholder for competition opportunities", cocurricular_id)
    create_file(service, "Employability_Enhancement_Programs.docx", "Placeholder for employability enhancement programs", cocurricular_id)
    
    # Create files in Support_Staff_Competences
    create_file(service, "Required_Competencies.docx", "Placeholder for required competencies", support_staff_id)
    create_file(service, "Deployment_Strategy.pdf", "Placeholder for deployment strategy", support_staff_id)
    create_file(service, "Roles_Relationships_Chart.pdf", "Placeholder for roles relationships chart", support_staff_id)
    
    # Create files in Service_Evaluation
    create_file(service, "Evaluation_Methods.docx", "Placeholder for evaluation methods", service_evaluation_id)
    create_file(service, "Benchmarking_Data.xlsx", "Placeholder for benchmarking data", service_evaluation_id)
    create_file(service, "Enhancement_Actions.xlsx", "Placeholder for enhancement actions", service_evaluation_id)def setup_facilities(service, parent_folder_id):
    """Set up the 7_Facilities_and_Infrastructure section."""
    logging.info("Setting up 7_Facilities_and_Infrastructure section...")
    
    # Create subfolders
    physical_resources_id = create_folder(service, "Physical_Resources", parent_folder_id)
    labs_equipment_id = create_folder(service, "Laboratories_Equipment", parent_folder_id)
    library_it_id = create_folder(service, "Library_IT_Resources", parent_folder_id)
    health_safety_id = create_folder(service, "Health_Safety_Environment", parent_folder_id)
    campus_env_id = create_folder(service, "Campus_Environment", parent_folder_id)
    support_staff_id = create_folder(service, "Support_Staff_Competences", parent_folder_id)
    facilities_eval_id = create_folder(service, "Facilities_Evaluation", parent_folder_id)
    
    # Create files in Physical_Resources
    create_file(service, "Resource_Inventory.xlsx", "Placeholder for resource inventory", physical_resources_id)
    create_file(service, "Sufficiency_Analysis.docx", "Placeholder for sufficiency analysis", physical_resources_id)
    create_file(service, "Resource_Allocation_Plan.pdf", "Placeholder for resource allocation plan", physical_resources_id)
    
    # Create files in Laboratories_Equipment
    create_file(service, "Lab_Equipment_Inventory.xlsx", "Placeholder for lab equipment inventory", labs_equipment_id)
    create_file(service, "Equipment_Maintenance_Records.xlsx", "Placeholder for equipment maintenance records", labs_equipment_id)
    create_file(service, "Equipment_Utilisation_Data.xlsx", "Placeholder for equipment utilisation data", labs_equipment_id)
    
    # Create files in Library_IT_Resources
    create_file(service, "Digital_Library_Resources.xlsx", "Placeholder for digital library resources", library_it_id)
    create_file(service, "IT_Systems_Documentation.docx", "Placeholder for IT systems documentation", library_it_id)
    create_file(service, "Network_Infrastructure_Map.pdf", "Placeholder for network infrastructure map", library_it_id)
    
    # Create files in Health_Safety_Environment
    create_file(service, "Health_Safety_Standards.pdf", "Placeholder for health safety standards", health_safety_id)
    create_file(service, "Accessibility_Measures.docx", "Placeholder for accessibility measures", health_safety_id)
    create_file(service, "Implementation_Evidence.pdf", "Placeholder for implementation evidence", health_safety_id)
    
    # Create files in Campus_Environment
    create_file(service, "Physical_Environment_Assessment.docx", "Placeholder for physical environment assessment", campus_env_id)
    create_file(service, "Social_Environment_Initiatives.pdf", "Placeholder for social environment initiatives", campus_env_id)
    create_file(service, "Psychological_Support_Services.docx", "Placeholder for psychological support services", campus_env_id)
    
    # Create files in Support_Staff_Competences
    create_file(service, "Facilities_Staff_Competencies.docx", "Placeholder for facilities staff competencies", support_staff_id)
    create_file(service, "Skills_Evaluation_Process.pdf", "Placeholder for skills evaluation process", support_staff_id)
    create_file(service, "Stakeholder_Needs_Assessment.xlsx", "Placeholder for stakeholder needs assessment", support_staff_id)
    
    # Create files in Facilities_Evaluation
    create_file(service, "Evaluation_Methods.docx", "Placeholder for evaluation methods", facilities_eval_id)
    create_file(service, "User_Satisfaction_Data.xlsx", "Placeholder for user satisfaction data", facilities_eval_id)
    create_file(service, "Enhancement_Plans.xlsx", "Placeholder for enhancement plans", facilities_eval_id)def setup_output_outcomes(service, parent_folder_id):
    """Set up the 8_Output_and_Outcomes section."""
    logging.info("Setting up 8_Output_and_Outcomes section...")
    
    # Create subfolders
    student_progression_id = create_folder(service, "Student_Progression", parent_folder_id)
    graduate_outcomes_id = create_folder(service, "Graduate_Outcomes", parent_folder_id)
    research_output_id = create_folder(service, "Research_Output", parent_folder_id)
    programme_outcomes_id = create_folder(service, "Programme_Outcomes", parent_folder_id)
    stakeholder_satisfaction_id = create_folder(service, "Stakeholder_Satisfaction", parent_folder_id)
    
    # Create files in Student_Progression
    create_file(service, "Pass_Rate_Data.xlsx", "Placeholder for pass rate data", student_progression_id)
    create_file(service, "Dropout_Rate_Analysis.xlsx", "Placeholder for dropout rate analysis", student_progression_id)
    create_file(service, "Time_to_Graduate_Statistics.xlsx", "Placeholder for time to graduate statistics", student_progression_id)
    create_file(service, "Benchmarking_Reports.pdf", "Placeholder for benchmarking reports", student_progression_id)
    
    # Create files in Graduate_Outcomes
    create_file(service, "Employability_Data.xlsx", "Placeholder for employability data", graduate_outcomes_id)
    create_file(service, "Entrepreneurship_Tracking.xlsx", "Placeholder for entrepreneurship tracking", graduate_outcomes_id)
    create_file(service, "Further_Studies_Data.xlsx", "Placeholder for further studies data", graduate_outcomes_id)
    create_file(service, "Improvement_Initiatives.docx", "Placeholder for improvement initiatives", graduate_outcomes_id)
    
    # Create files in Research_Output
    create_file(service, "Staff_Research_Output.xlsx", "Placeholder for staff research output", research_output_id)
    create_file(service, "Student_Research_Output.xlsx", "Placeholder for student research output", research_output_id)
    create_file(service, "Research_Benchmarking.docx", "Placeholder for research benchmarking", research_output_id)
    
    # Create files in Programme_Outcomes
    create_file(service, "Outcome_Achievement_Data.xlsx", "Placeholder for outcome achievement data", programme_outcomes_id)
    create_file(service, "Monitoring_Process.docx", "Placeholder for monitoring process", programme_outcomes_id)
    create_file(service, "Outcome_Improvement_Plan.xlsx", "Placeholder for outcome improvement plan", programme_outcomes_id)
    
    # Create files in Stakeholder_Satisfaction
    create_file(service, "Satisfaction_Survey_Instruments.docx", "Placeholder for satisfaction survey instruments", stakeholder_satisfaction_id)
    create_file(service, "Satisfaction_Data_Analysis.xlsx", "Placeholder for satisfaction data analysis", stakeholder_satisfaction_id)
    create_file(def setup_sar_reports(service, parent_folder_id):
    """Set up the SAR_Reports section."""
    logging.info("Setting up SAR_Reports section...")
    
    # Create subfolders
    previous_sars_id = create_folder(service, "Previous_SARs", parent_folder_id)
    sar_templates_id = create_folder(service, "SAR_Templates", parent_folder_id)
    assessment_results_id = create_folder(service, "Assessment_Results", parent_folder_id)
    feedback_reports_id = create_folder(service, "Feedback_Reports", parent_folder_id)
    
    # Create files in Previous_SARs
    create_file(service, "SAR_2022.pdf", "Placeholder for SAR 2022", previous_sars_id)
    create_file(service, "SAR_2023.pdf", "Placeholder for SAR 2023", previous_sars_id)
    create_file(service, "SAR_2024.pdf", "Placeholder for SAR 2024", previous_sars_id)
    
    # Create files in SAR_Templates
    create_file(service, "AUN_QA_SAR_Template.docx", "Placeholder for AUN-QA SAR template", sar_templates_id)
    create_file(service, "Evidence_Checklist.xlsx", "Placeholder for evidence checklist", sar_templates_id)
    
    # Create files in Assessment_Results
    create_file(service, "Internal_Assessment_Results.pdf", "Placeholder for internal assessment results", assessment_results_id)
    create_file(service, "External_Assessment_Results.pdf", "Placeholder for external assessment results", assessment_results_id)
    
    # Create files in Feedback_Reports
    create_file(service, "Assessor_Feedback.docx", "Placeholder for assessor feedback", feedback_reports_id)
    create_file(service, "Stakeholder_Feedback_on_SAR.xlsx", "Placeholder for stakeholder feedback on SAR", feedback_reports_id)def setup_quality_improvement(service, parent_folder_id):
    """Set up the Quality_Improvement_Plans section."""
    logging.info("Setting up Quality_Improvement_Plans section...")
    
    # Create subfolder
    progress_reports_id = create_folder(service, "Progress_Reports", parent_folder_id)
    
    # Create files in Quality_Improvement_Plans
    create_file(service, "Annual_Improvement_Plan.xlsx", "Placeholder for annual improvement plan", parent_folder_id)
    create_file(service, "Improvement_Actions_Tracking.xlsx", "Placeholder for improvement actions tracking", parent_folder_id)
    create_file(service, "PDCA_Cycle_Documentation.docx", "Placeholder for PDCA cycle documentation", parent_folder_id)
    
    # Create files in Progress_Reports
    create_file(service, "Quarter_1_Progress.pdf", "Placeholder for Q1 progress report", progress_reports_id)
    create_file(service, "Quarter_2_Progress.pdf", "Placeholder for Q2 progress report", progress_reports_id)
    create_file(service, "Quarter_3_Progress.pdf", "Placeholder for Q3 progress report", progress_reports_id)
    create_file(service, "Quarter_4_Progress.pdf", "Placeholder for Q4 progress report", progress_reports_id)def main():
    """Main function to set up the AUN-QA folder structure."""
    try:
        # Get credentials and build the service
        logging.info("Starting AUN-QA folder structure creation...")
        creds = get_credentials()
        service = build('drive', 'v3', credentials=creds)
        
        # Prompt user for parent folder ID (optional)
        parent_folder_id = input("Enter parent folder ID (or press Enter to create in root): ").strip() or None
        
        # Setup main structure
        folder_structure, aun_qa_folder_id = setup_aun_qa_structure(service, parent_folder_id)
        
        # Setup individual sections
        setup_programme_overview(service, folder_structure["0_Programme_Overview"])
        setup_expected_learning_outcomes(service, folder_structure["1_Expected_Learning_Outcomes"])
        setup_programme_structure(service, folder_structure["2_Programme_Structure_and_Content"])
        setup_teaching_learning(service, folder_structure["3_Teaching_and_Learning_Approach"])
        setup_student_assessment(service, folder_structure["4_Student_Assessment"])
        setup_academic_staff(service, folder_structure["5_Academic_Staff"])
        setup_student_support(service, folder_structure["6_Student_Support_Services"])
        setup_facilities(service, folder_structure["7_Facilities_and_Infrastructure"])
        setup_output_outcomes(service, folder_structure["8_Output_and_Outcomes"])
        setup_sar_reports(service, folder_structure["SAR_Reports"])
        setup_quality_improvement(service, folder_structure["Quality_Improvement_Plans"])
        
        logging.info(f"AUN-QA folder structure created successfully! Main folder ID: {aun_qa_folder_id}")
        print(f"\nAUN-QA folder structure created successfully!")
        print(f"Main folder ID: {aun_qa_folder_id}")
        print("Check the log file (aun_qa_creation.log) for details of all created folders and files.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        print("Check the log file for more details.")

if __name__ == '__main__':
    main()