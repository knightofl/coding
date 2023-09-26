import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}
c = ['name', 'subject', 'score', 'grade', 'etc']

df = pd.DataFrame(data=score, columns=c)
print(df)
print()

print(df['name'])
print()

print(df.name)
print()

print(df[['name', 'subject', 'grade']])
print()

print(type(df[['name', 'subject', 'grade']]))
print()

print(df.loc[1])
print()

print(type(df.loc[1]))
print()

print(df.loc[[0,2,4]])
print()

df.loc[0] = ['Jessi', 'java', 70, 'C', 1]
print(df)
print()

row_idx = [1, 2, 4]
col_idx = ['name', 'subject', 'grade']
print(df.loc[row_idx, col_idx])
print()