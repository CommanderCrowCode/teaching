from pandas import read_csv, concat
import pandas as pd
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

def column_to_lower(df):
  df.columns = [x.lower().replace(' ', '_') for x in df.columns]
  return df

def process_csv_list(csv_list):
  df = combine_csvs_to_df(csv_list)
  df = column_to_lower(df)
  return df

def zipgrade_extract(input_df):
  output = input_df[['zipgrade_id','num_questions','num_correct']].copy()
  output.rename(columns={
    'zipgrade_id':'student_id',
    }, inplace=True)
  return output



# Handling current roster
student = process_csv_list(student_list)
student.drop(['field_of_study', 
              'major',
              'registration_type',
              'credit','gpa','study_status'
              ],
             axis=1, inplace=True)
# Fill NA for registration status
student['registration_status'].fillna(True, inplace=True)

# Process CPR practical
cpr_practical = process_csv_list(cpr_practical_list)
cpr_practical = cpr_practical[['zipgrade_id','num_questions','num_correct']].copy()
cpr_practical.rename(columns={
  'zipgrade_id':'student_id',
  'num_questions':'cpr_practical_num_questions',
  'num_correct':'cpr_practical_num_correct'
  }, inplace=True)
# count number of digits in 'student_id' column
cpr_practical['id_digit_count'] = cpr_practical['student_id'].astype(str).str.len()
cpr_practical['id_digit_error'] = (cpr_practical['id_digit_count'] != 10)

first_aid_practical = process_csv_list(first_aid_list)
first_aid_practical = zipgrade_extract(first_aid_practical)
written = process_csv_list(written_list)
written = zipgrade_extract(written)

# export all dataframes to xlsx
with pd.ExcelWriter('output.xlsx') as writer:
  student.to_excel(writer, sheet_name='student')
  cpr_practical.to_excel(writer, sheet_name='cpr_practical')
  first_aid_practical.to_excel(writer, sheet_name='first_aid_practical')
  written.to_excel(writer, sheet_name='written')





# if cpr_practical['id_digit_error'].any():
#   # Reset index and store under column
#   cpr
#   # get row index of error
#   error_index = cpr_practical[cpr_practical['id_digit_error'] == True].index.tolist()
#   print('What!')



# grade_items = [cpr_practical, first_aid_practical, written]


# practical = read_csv(practical_list)

# current = practical[practical['student_id'].isin(student['ID number'])]
# current.to_csv(output)

