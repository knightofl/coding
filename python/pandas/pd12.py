from os import O_EXCL
import pandas as pd


d = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
     'score': [100, 95, 80, 85, 97],
     'grade': ['A', 'A', 'B', 'B', 'A'],
     'subject':['python', 'java', 'python', 'c', 'java']}

sample_df = pd.DataFrame(data=d)
print(sample_df)
print()

sample_df.set_index('name', inplace=True)
print(sample_df)
print()

subset = sample_df[1:4]
print(subset)
print()

subset = sample_df[::2]
print(subset)
print()

subset = sample_df[:'Alex']
print(subset)
print()

subset = sample_df.loc[:'Emma', ['subject', 'grade']]
print(subset)
print()

subset = sample_df.iloc[:3, -1]
print(subset)
print()
