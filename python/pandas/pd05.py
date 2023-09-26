import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'age': [20, 24, 23, 20, 27],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}

score_df = pd.DataFrame(data=score)
print(score_df)
print()

print(score_df.describe())
print()

print(score_df[['grade', 'subject']].describe())
print()

print(score_df.describe(include='all'))
print()

print(score_df['subject'].unique())
print()

print(score_df['subject'].value_counts())
print()

print(score_df['subject'].value_counts(normalize=True))
print()