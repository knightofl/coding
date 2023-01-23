import numpy as np
import pandas as pd


df = pd.DataFrame(data = np.arange(18).reshape(6,3),
				  index = ['a','b','c','d','e','f'],
                  columns=['col1','col2','col3'])

print(df)
print()

df['col4'] = pd.Series(data = [1.7, 1.2, 2.4], 
                       index = ['a','e','c'])
print(df)
print()

df.loc['c'] = None
print(df)
print()

print(df.info())
print()

print(df.isnull())
print()

print(df.isnull().sum())
print()

print(df.isnull().sum(axis=1))
print()

print(df.dropna())
print()

print(df)
print()

print(df.dropna(how='all'))
print()

print(df)
print()

df.dropna(how='all', inplace=True)
print(df)
print()

print(df)
print()

print(df.dropna(axis='columns'))
print(df)
print()

df.iloc[:2, 0] = np.nan
df.iloc[:4, 1] = np.nan
print(df)
print()

print(df.fillna(0))
print()

replace_set = {'col2':10, 'col4':'100'}
print(df.fillna(replace_set))
print()

replace_set = {'col1':df['col1'].mean()}
df.fillna(replace_set, inplace=True)
print(df)
print()

