import pandas as pd

tt = pd.read_csv('./practice/titanic_train.csv')
print(tt, tt.dtypes)

print(tt.head())
print(tt.tail())

dic1 = {'name': ['철민', '은경', '진웅', '수범'],
        'year': [2011, 2015, 2016, 2014],
        'sex': ['남', '녀', '남', '남']
        }

dd = pd.DataFrame(dic1)
print(dd, dd.dtypes)

dd = pd.DataFrame(dic1, columns=['name', 'year', 'sex', 'age'])
print (dd)

dd = pd.DataFrame(dic1, index=['one', 'two', 'three', 'four'])
print(dd)

print('컬럼', tt.columns)
print('인덱스', tt.index)
print('인덱스 벨류', tt.index.values)

ser_tt = tt['Name']
print(ser_tt.head(), type(ser_tt))

filtered_tt = tt[['Name', 'Age']]
print(filtered_tt.head(), type(filtered_tt))

col_tt = tt[['Name']]
print(col_tt.head(), type(col_tt))

print(ser_tt.shape)
print(col_tt.shape)

print(tt.info())
print(tt.describe())
print(tt['Sex'].value_counts())

print(tt[['Name', 'Age']].sort_values(by='Age'))

print(tt.head().values.tolist())
print(tt.head().to_dict('list'))

