import numpy as np
import pandas as pd


score = {'sub1': [3, 9, 1, 1, 9],
         'sub2': [2, 9, np.nan, np.nan, 8],
         'sub3': [np.nan, 1, 5, 5, 7],
         'sub4': [np.nan, 3, np.nan, 1, np.nan]}

df = pd.DataFrame(data=score)
print(df)
print()

print(df.count())
print()

print(df.count(axis=1))
print()

print(df.sum())
print()

print(df.sum(skipna=False))
print()
