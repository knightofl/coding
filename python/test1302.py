import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

even = np.arange(1, 101)
even_df = pd.DataFrame(even)
print(even_df)

plt.plot(even, even)
plt.show()

plt.plot(even_df, even_df ** 2)
plt.show()
