import pandas as pd


titanic_df = pd.read_csv('titanic.csv')
#print(titanic_df)
print(type(titanic_df))
print()

print(titanic_df.info())
print()

print(titanic_df.head())
print()

