import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')

#exl = pd.read_excel('./practice/101_DT.xlsx')
exl = pd.read_excel('./practice/101_DT.xlsx', header=1)
print('\n액셀\n', exl.tail())
print(exl.columns)

mask_df = exl[(exl['전출지별'] == '서울특별시')
        & (exl['전입지별'] != '서울특별시')
        & (exl['항목'] == '이동자수')]
print('\n마스크\n', mask_df)
print(mask_df.columns)
print('\n리스트\n', list(mask_df))

mask_fn = mask_df.fillna(0)
sort_df = mask_fn[list(mask_fn)[:2] + sorted(list(mask_fn)[4:])]
print('\n소트\n', sort_df)
print('\n리스트\n', list(sort_df))

sort_df = sort_df.drop(columns=['전출지별'], axis=0)
print(sort_df)

sort_df.set_index('전입지별', inplace=True)
print(sort_df)

ex1_df = sort_df.loc['경기도']
print(ex1_df)
print(ex1_df.index)
print(ex1_df.values)

plt.plot(ex1_df.index, ex1_df.values)
plt.title('서울 => 경기')
plt.xlabel('시기')
plt.ylabel('인구수')
plt.show()

plt.figure(figsize=(20,5))
plt.plot(ex1_df.index, ex1_df.values, label='서울 => 경기')
plt.xticks(rotation='vertical')
plt.title('서울 => 경기')
plt.xlabel('시기')
plt.ylabel('인구수')
plt.show()

print(plt.style.available)

plt.figure(figsize=(20,5))
plt.style.use('bmh')
plt.plot(ex1_df.index, ex1_df.values, label='서울 => 경기')
plt.xticks(rotation='vertical')
plt.title('서울 => 경기')
plt.xlabel('시기')
plt.ylabel('인구수')
plt.show()

ex2_df = sort_df.loc[['부산광역시', '인천광역시', '대전광역시'], ['2000 년', '2009 년']]
print(ex2_df)
#plt.plot(ex2_df, kind='bar')
ex2_df.plot(kind='bar')
plt.show()

#years = list(map(lambda x: str(x)+" 년", range(2000,2020)))
years = [str(x)+" 년" for x in range(2000,2020)]

ex3_df = sort_df.loc[['부산광역시', '인천광역시', '대전광역시'], [str(x)+" 년" for x in range(2000,2020)]]
print(ex3_df)
ex3_df.plot(kind='bar')
plt.show()

ex4_df = ex3_df.transpose()
ex4_df.plot(kind='bar')
plt.show()