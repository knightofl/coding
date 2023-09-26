import pandas as pd

tt = pd.read_csv('./practice/titanic_train.csv')

tt['New_Age'] = tt['Age']+1
print(tt.tail())

tt.drop('New_Age', axis=1, inplace=True)
print(tt.tail())

tt.drop(890, axis=0, inplace=True)
print(tt.tail())

print('\ncolumns\n', tt.columns, type(tt.columns))
print('\nindex\n', tt.index)
print('\ncolumns vlaues\n', tt.columns.values, type(tt.columns.values))
print('\nindex values\n', tt.index.values, tt.index.values.shape)

# tt.index[889] = 900
print(tt.index[889])
print(tt.index[:5])

ser_age = tt['Age']
print(ser_age.max())
print(ser_age.min())
print(ser_age.sum())
print(ser_age.mean())
print((ser_age + 5).tail())

print(tt['Pclass'].value_counts())
print(tt['Sex'].value_counts())
print(tt['Embarked'].value_counts())
tt2 = tt['Embarked'].value_counts().reset_index(inplace=False)
print(tt2)

print(tt.iloc[1,3])
print(tt.loc[1, 'Name'])

print(tt[tt['Age'] > 60][['Name', 'Age']])
print(tt[['Name', 'Age']][tt['Age'] > 60])
print(tt[['Name', 'Age']][(tt['Age'] > 60) & (tt['Sex'] == 'female')])

print(tt[['Age', 'Fare']].mean(axis=0))
print(tt[['Age', 'Fare']].mean(axis=1))
print(tt[['Age', 'Fare']].count())

print(tt.groupby(by='Sex').count())
print(tt.groupby(by='Sex').count().shape)
print(tt.groupby(by='Sex').count().index)

print(tt.groupby(by='Pclass')[['PassengerId', 'Survived']].count())
print(tt.groupby(by='Pclass')['Age'].agg([max, min]))
print(tt.groupby(by='Pclass').agg({'Age':'max', 'SibSp':'sum', 'Fare':'mean'}))

print(tt.isna().tail())
print(tt.isna().sum())

tt['Cabin'] = tt['Cabin'].fillna('C000')
print(tt['Cabin'])

tt['Name_Len'] = tt['Name'].apply(lambda x: len(x))
print(tt.tail())

tt['Adult'] = tt['Age'].apply(lambda x: 'Child' if x<15 else 'Teen' if x<20 else 'Adult')
print(tt.groupby(by='Adult').count())
print(tt['Adult'].value_counts())

def getCat(age):
    cat = ''
    if age < 5: cat = 'baby'
    elif age < 10: cat = 'child'
    elif age < 20: cat = 'teen'
    else: cat = 'kidult'
    return cat

tt['Adult'] = tt['Age'].apply(lambda x: getCat(x))
print(tt['Adult'].value_counts())

