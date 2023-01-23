import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston


boston = load_boston()
boston_df = pd.DataFrame(boston.data,
                         columns = boston.feature_names)
boston_df['price'] = boston.target
boston_df.head()

plt.hist(boston_df['price'], bins=10)
plt.xlabel('Price', fontsize=14)
plt.show()

plt.scatter(x='RM', y='price', data=boston_df)
plt.xlabel('RM', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.show()
