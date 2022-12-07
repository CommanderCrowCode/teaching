import pandas as pd
from pandas import read_csv

past_grades_files = [
  'section1_1_2564.csv',
  'section2_1_2564.csv',
  'section1_2_2564.csv',
  'section2_2_2564.csv'
]

practical_file = 'practical_cpr.csv'

def check_student_id_series(student_id:pd.Series) -> bool:
  target_length = 10
  truth_value = student_id.astype(str).apply(lambda x: len(x) == target_length).all()
  return truth_value

current_grades = read_csv('all_grades.csv')
current_grades['Written test total (Real)'] = current_grades['Written test total (Real)'].replace('-',0)
current_grades['Practical test total (Real)'] = current_grades['Practical test total (Real)'].replace('-',0)
current_grades['Written test total (Real)'] = current_grades['Written test total (Real)'].astype(float)
current_grades['Practical test total (Real)'] = current_grades['Practical test total (Real)'].astype(float)
current_grades = current_grades.rename({'Written test total (Real)':'written','Practical test total (Real)':'practical'},axis=1)

# Calculate who got certified for this semester
current_grades['written_pass'] = current_grades['written'] >= 69.5
current_grades['practical_pass'] = current_grades['practical'] >= 69.5
current_grades['certified'] = (current_grades['written_pass'] & current_grades['practical_pass'])
current_grades['certified'] = current_grades['certified'].replace({True:'Yes',False:'No'})
current_grades.to_csv('certification.csv')

# Pulling out certification from this year as well as current year students
current_year_students = current_grades['ID number']
current_semester_cert = current_grades[current_grades['certified']=='Yes'] \
  [['First name','Surname','ID number']]
print("Checking for validity of ID number before exporting....")
all_valid = check_student_id_series(current_semester_cert['ID number'])
# If not valid, throw an error
if not all_valid:
  raise ValueError("Not all IDs are valid")

current_semester_cert.to_excel('~/Desktop/current_semester_cert.xlsx')

# collecting past grades
past_grades = [
  pd.read_csv(file,index_col=1)
  for file in past_grades_files
]

past_grades = pd.concat(past_grades)
past_grades = past_grades.drop('Unnamed: 0',axis=1)
past_grades = past_grades.rename({'STUDENT ID':'student_id'},axis=1)
past_grades = past_grades[['student_id','NAME','GRADE']].copy()
past_grades.columns = ['student_id','name','grade']
# selecting only people who have passed the written benchmarks

acceptable_grades = ['A+','A','B+','B','C+','C']
past_grades_with_written = past_grades[past_grades['grade'].isin(acceptable_grades)]

# Get all practical tests from this semester
practical = pd.read_csv(practical_file,index_col=1)
practical = practical[['student_id','Percent Correct']]

# Correcting known bad student id
practical = practical.replace(643021405, 6430314005)

print("Checking for validity of ID number for practical tests...")
all_valid = check_student_id_series(practical['student_id'])
# If not valid, throw an error
if not all_valid:
  raise ValueError("Not all IDs are valid")

# Get practical score that do not belong to this year students
extra_practical = practical[~practical['student_id'].isin(current_year_students)]
extra_cert = pd.merge(extra_practical, past_grades_with_written, how='inner', on = 'student_id')

extra_cert = extra_cert[['name','student_id']]
extra_cert.to_csv('extra_cert.csv')
extra_cert.to_excel('~/Desktop/extra_cert.xlsx')