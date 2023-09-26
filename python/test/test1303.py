import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')

#even = np.arange(1, 101)
even = [x for x in range(1, 101)]
print(even)
even_df = pd.DataFrame(even, columns=['no'])

even_df.index = even_df.index + 1
print(even_df)

even_df['pow'] = even_df['no'] ** 2
print(even_df)

plt.plot(even_df.index, even_df['pow'], label='pow')
plt.plot(even_df.index, even_df['no']*10, label='y=x*10')
plt.legend()
#plt.savefig('graph.png')
plt.show()
