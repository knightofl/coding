import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic_df = sns.load_dataset('titanic')
print(titanic_df.info())
print()

result = titanic_df['class'].value_counts()
print(result)

x = result.index
y = result.values

plt.bar(x, y)
plt.show()

colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
plt.pie(y, labels=x, colors=colors, autopct='%1.1f%%', startangle=90)
plt.show()
