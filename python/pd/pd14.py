import numpy as np
import pandas as pd


sample = {'product':['a','b','a','b','a','b','a','a'],
          'sensor':['s1','s1','s2','s3','s2','s2','s1','s3'],
          'x':np.arange(1,9),
          'y':np.arange(5,13)}

df = pd.DataFrame(data=sample)
print(df)
print()

grouped_product = df.groupby('product')
print(grouped_product)
print()

for key, value in grouped_product:
    print('------------------------')
    print('key : ', key)
    print('value : \n', value)
    print('------------------------')
print()

grouped_product = df.groupby('product').sum()
print(grouped_product)
print()

grouped_product = df.groupby(['product', 'sensor']).sum()
print(grouped_product)
print()

grouped_product = df.groupby(['product', 'sensor'])['x'].sum()
print(grouped_product)
print()

condition = {'x':'max', 'y':'min'}
grouped_product =df.groupby(['product', 'sensor']).agg(condition)
print(grouped_product)
print()
