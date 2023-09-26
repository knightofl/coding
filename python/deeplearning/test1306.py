import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')

m = 100
f = 150
m_p = m / (m+f)
f_p = f / (m+f)

color = ['blue', 'red']
label = ['male', 'female']

plt.figure(figsize = (6, 6))
patches, texts = plt.pie([m_p, f_p], labels=label, colors=color)
print(patches)
print(texts)
plt.show()
