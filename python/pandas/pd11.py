import pandas as pd


d = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
     'score': [100, 95, 80, 85, 97],
     'grade': ['A', 'A', 'B', 'B', 'A'],
     'subject': ['python', 'java', 'python', 'c', 'java']}

df = pd.DataFrame(data=d)
print(df)
print()

df.set_index('name', inplace=True)
print(df)
print()

print(df.loc['Emma', 'score'])
print()

subset = df.loc[['Jessi', 'Emma']]
print(subset)
print()

subset = df.iloc[[0, 4]]
print(subset)
print()

subset = df.loc[df['score'] >= 95]
print(subset)
print()

subset = df.loc[df['subject'] == 'python']
print(subset)
print()


