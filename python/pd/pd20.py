import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


anscombe_df = sns.load_dataset('anscombe')
print(anscombe_df)
print()

categorical = anscombe_df.dataset.unique()
print(categorical)
print()

dataset_1 = anscombe_df[anscombe_df['dataset'] == categorical[0]]
dataset_2 = anscombe_df[anscombe_df['dataset'] == categorical[1]]
dataset_3 = anscombe_df[anscombe_df['dataset'] == categorical[2]]
dataset_4 = anscombe_df[anscombe_df['dataset'] == categorical[3]]

print(dataset_2)
print()

print(dataset_2.describe())
print()

plt.figure()
plt.subplot(221)
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.title('dataset_1')

plt.subplot(222)
plt.plot(dataset_2['x'], dataset_2['y'], 'o')
plt.title('dataset_2')

plt.subplot(223)
plt.plot(dataset_3['x'], dataset_3['y'], 'o')
plt.title('dataset_3')

plt.subplot(224)
plt.plot(dataset_4['x'], dataset_4['y'], 'o')
plt.title('dataset_4')

plt.tight_layout()
plt.show()

plt.figure()
plt.plot(dataset_1['x'], dataset_1['y'], 'o')
plt.plot(dataset_2['x'], dataset_2['y'], '<')
plt.plot(dataset_3['x'], dataset_3['y'], '>')
plt.plot(dataset_4['x'], dataset_4['y'], 'x')
plt.title('dataset 1234')
plt.show()
