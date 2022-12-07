from pandas import read_csv

all_grades = read_csv('all_grades.csv')
all_grades['Written test total (Real)'] = all_grades['Written test total (Real)'].replace('-',0)
all_grades['Practical test total (Real)'] = all_grades['Practical test total (Real)'].replace('-',0)
all_grades['Written test total (Real)'] = all_grades['Written test total (Real)'].astype(float)
all_grades['Practical test total (Real)'] = all_grades['Practical test total (Real)'].astype(float)
all_grades = all_grades.rename({'Written test total (Real)':'written','Practical test total (Real)':'practical'},axis=1)

all_grades['written_pass'] = all_grades['written'] >= 69.5
all_grades['practical_pass'] = all_grades['practical'] >= 69.5
all_grades['certified'] = (all_grades['written_pass'] & all_grades['practical_pass'])
all_grades['certified'] = all_grades['certified'].replace({True:'Yes',False:'No'})
all_grades.to_csv('certification.csv')
