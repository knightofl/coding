import pandas as pd


print(pd.__version__)
print()

year = ['2019', '2020', '2021', '2022']
result = pd.Series(data=year)

print('Type : ', type(result))
print()

print(result)
print()

print('Index : ', result.index)
print('Data : ', result.values)
print('Dtype : ', result.dtype)
print('Shape : ', result.shape)
print()

result.name = 'Year'
result.index.name = 'No.'
print(result)
print()

idx = ['a', 'b', 'c', 'd']
result = pd.Series(data=year, index=idx, name='Year')
print(result)
print()

score = {'Kim':85, 'Han':89, 'Lee':89, 'Choi':70}
result = pd.Series(data=score,name='Score')
print(result)
print()