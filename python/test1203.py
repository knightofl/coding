import pandas as pd

tt = pd.read_csv('./practice/titanic_train.csv')
print(tt.head())
print(tt.tail())

print('\ncolumns\n', tt.columns)
print('\nindex\n', tt.index)
print('\ncolumns vlaues\n', tt.columns.values)
print('\nindex values\n', tt.index.values)


dic1 = {'name': ['철민', '은경', '진웅', '수범'],
        'year': [2011, 2015, 2016, 2014],
        'sex': ['남', '녀', '남', '남']
        }

dd1 = pd.DataFrame(dic1)
print('\nDataFrame\n', dd1)
print('\ndtypes\n', dd1.dtypes)


dd2 = pd.DataFrame(dd1, columns=['name', 'year', 'sex', 'age'])
print()
print(dd2)

dd2 = pd.DataFrame(dic1, index=['하나', '둘', '셋', '넷'])
#dd2 = pd.DataFrame(dd1, index=['하나', '둘', '셋', '넷'])
print()
print(dd2)

series_tt = tt['Name']
print('\nseries\n', series_tt)

filtered_tt = tt[['Name', 'Age']]
print('\nfiltered\n', filtered_tt)

df_tt = tt[['Name']]
print('\ndata frame\n', df_tt)
print(type(series_tt), type(filtered_tt), type(df_tt))
print(series_tt.shape, filtered_tt.shape, df_tt.shape)
print(series_tt.ndim, filtered_tt.ndim, df_tt.ndim)

print('\ninfo\n', tt.info)
print('\ndescribe\n', tt.describe)

#print(tt[['Sex']].value_counts())
print('\nvalue_counts\n', tt['Sex'].value_counts())

print('\nsort\n', tt[['Name', 'Age']].sort_values(by='Age'))
print('\nsort\n', tt[['Name', 'Age']].sort_values(by='Name', ascending=False))

print('\nvalues\n', tt.values)
print('\nto list\n', tt.values.tolist())
print('\nto dict\n', tt.to_dict())
print('\nto dict list\n', tt.to_dict('list'))
