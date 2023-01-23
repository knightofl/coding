import pandas as pd


sample_df = pd.read_excel('students_score.xlsx')
print(sample_df.info())
print()

print(sample_df.head())
print()

sample_df = pd.read_excel('students_score.xlsx', header=None)
sample_df.columns = ['name', 'age', 'score', 'grade', 'subject']
print(sample_df.head())
print()

students_df = pd.read_excel('students_score.xlsx', sheet_name='students')
print(students_df.head())

