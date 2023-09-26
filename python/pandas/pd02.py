from numpy import PINF
import pandas as pd


score = {'name': ['Jessi', 'Emma', 'Alex', 'Tom'],
         'score': [100, 95, 80, 85],
         'grade': ['A', 'A', 'B', 'B']}

df = pd.DataFrame(data=score)

print(type(df))
print()

print(df)
print()

print('Index : ', df.index)
print('Columns : ', df.columns)
print('Values : ', df.values)
print('Dtype : ', df.dtypes)
print('Shape : ', df.shape)