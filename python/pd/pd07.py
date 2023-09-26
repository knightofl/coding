import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}
c = ['name', 'subject', 'score', 'grade', 'etc']

df = pd.DataFrame(data=score, columns=c)
print(df)
print()

semester_data = pd.Series(['20-01', '20-01', '20-02', '20-01'])
df['semester'] = semester_data
print(df)
print()

df['high_score'] = df['score'] > 90
print(df)
print()

df.loc[6] = ['Jina', 'python', 100, 'A', 1, '20-02', True]
print(df)
print()

df.drop(6)
print(df)
print()

result = df.drop(6)
print(result)
print()

df.drop(6, inplace=True)
print(df)
print()

result = df.drop(columns=['etc'])
print(result)
print()

print(df)
print()

df.drop(columns=['etc'], inplace=True)
print(df)
print()

