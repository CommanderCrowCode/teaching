from pandas import read_csv

student_list = './student_list.csv'
practical_list = './practical_cpr.csv'
output = '/Users/tanwa/Desktop/current.csv'

student = read_csv(student_list)
practical = read_csv(practical_list)

current = practical[practical['student_id'].isin(student['ID number'])]
current.to_csv(output)

