import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplothan


bike_data = pd.read_csv('bike_2101_utf8_0618.csv')
print(bike_data.info())
print()

print(bike_data.head())
print()

print(bike_data.tail())
print()

print(bike_data.shape)
print()

print(bike_data.describe())
print()

print(bike_data['대여구분코드'].unique())
print()

print(bike_data['대여구분코드'].value_counts())
print()

print(bike_data['대여구분코드'].value_counts(normalize=True))
print()

print(bike_data['운동량'].unique())
print()

print(bike_data['운동량'].describe())
print()

print(bike_data['운동량'].isnull().sum())
print()

pattern = '([0-9])'
bike_data['temp'] = bike_data['운동량'].str.match(pattern)
print(bike_data['temp'])
print()

print(bike_data['temp'].sum())
print()

print(bike_data.loc[bike_data['temp']==False, '운동량'])
print()

bike_data.drop(columns=['temp'], inplace=True)
bike_data.loc[bike_data['운동량']=='\\N', '운동량'] = np.NaN
print(bike_data['운동량'].isnull().sum())
print()

bike_data['운동량'] = bike_data['운동량'].astype(float)
print(bike_data.info())
print()

bike_data.loc[bike_data['탄소량']=='\\N', '탄소량'] = np.NaN
print(bike_data['탄소량'].isnull().sum())
print()

bike_data['탄소량'] = bike_data['탄소량'].astype(float)
print(bike_data.info())
print()

print(bike_data.isnull().sum())
print()

print(bike_data['성별'].unique())
print()

print(bike_data['성별'].value_counts())
print()

bike_data['성별'] = bike_data['성별'].str.upper()
print(bike_data['성별'].value_counts())
print()

result = bike_data['성별'].value_counts()
result.plot.pie(autopct='%1.1f%%')
plt.show()

print(bike_data['성별'].isnull().sum())
print()

con = {'성별':'U'}
bike_data.fillna(con, inplace=True)

print(bike_data['성별'].isnull().sum())
print()

result = bike_data['성별'].value_counts()
result.plot.pie(autopct='%1.1f%%')
plt.show()

print(bike_data.isnull().sum())
print()

print(bike_data['운동량'].mean())
print(bike_data['탄소량'].mean())
print()

con = {'운동량':bike_data['운동량'].mean()}
bike_data.fillna(con, inplace=True)
#bike_data.dropna(inplace=True)
con = {'탄소량':bike_data['탄소량'].mean()}
bike_data.fillna(con, inplace=True)

print(bike_data.isnull().sum())
print()

# IQR 활용한 이상치 함수 구현
def outliers_iqr(data, iqr_range):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - (iqr * iqr_range)
    upper_bound = q3 + (iqr * iqr_range)
    return data[(data > upper_bound) | (data < lower_bound)].index

outliers = outliers_iqr(bike_data['이동거리'], 1.5)
print(outliers.size)
print()

print(bike_data.iloc[outliers])
print()

bike_data.drop(outliers, inplace=True)
print(bike_data.describe())


bike_station = pd.read_csv('bike_station_2101.csv', encoding='cp949', header=4)
print(bike_station.info())
print()

bike_station = bike_station.iloc[:, 0:6]
bike_station.columns = ['대여소번호', '보관소', '소재지', '주소', '위도', '경도']

print(bike_station.head())
print(bike_station.info())
print()

print(bike_station.isnull().sum())
print()

print(bike_station[bike_station['대여소번호'].isnull()])
print()

bike_station.dropna(how='all', inplace=True)
print(bike_station.isnull().sum())
print()

bike_station['대여소번호'] = bike_station['대여소번호'].astype(int)
print(bike_station.info())
print()

subset = bike_station[['대여소번호', '소재지']]
print(subset.head())
print()

merge_data = pd.merge(bike_data, subset, on='대여소번호')
print(merge_data.head())
print()

result = merge_data.groupby(['성별'])['이용건수'].sum()
print(result)
print()

print(result.sort_values())
print()

print(result.sort_values(ascending=False))
print()

result = merge_data.groupby(['연령대코드'])['이용건수'].sum().sort_values(ascending=False)
print(result)
print()

x = result.index
y = result.values
plt.bar(x, y)
plt.show()

result = merge_data.groupby(['대여일자'])['이용건수'].sum()
print(result)
print()

x = result.index
y = result.values
plt.figure(figsize=(16,8))
plt.plot(x, y)
plt.xticks(rotation=45)
plt.show()

result = merge_data.groupby(['소재지'])['이용건수'].sum().sort_values()
print(result)
print()

x = result.index
y = result.values
plt.bar(x, y)
plt.xticks(rotation=45)
plt.show()