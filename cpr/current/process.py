from pandas import read_csv, concat
from glob import glob

# Settings
output = '/Users/tanwa/Desktop/current.csv'

# list all file under raw_data directory
student_list = glob('./raw_data/student*.csv')
first_aid_list = glob('./raw_data/first_aid*.csv')
cpr_practical_list = glob('./raw_data/cpr_practical*.csv')
written_list = glob('./raw_data/written*.csv')

def combine_csvs_to_df(csv_list):
  df = read_csv(csv_list[0])
  for i in range(1, len(csv_list)):
    data = read_csv(csv_list[i])
    df = concat([df,data])
  return df


# Handling current roster
student = combine_csvs_to_df(student_list)
# For all columns in student, rename to lower letter and replace whitespace with underscore
student.columns = [x.lower().replace(' ', '_') for x in student.columns]
# Drop unnecessary columns
student.drop(['field_of_study', 
              'major',
              'registration_type',
              'credit','gpa','study_status'
              ],
             axis=1, inplace=True)
# Fill NA for registration status
student['registration_status'].fillna(True, inplace=True)


practical_list = './practical_cpr.csv'

student = read_csv(student_list)
practical = read_csv(practical_list)

current = practical[practical['student_id'].isin(student['ID number'])]
current.to_csv(output)

