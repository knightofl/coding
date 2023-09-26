import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothicCoding')

ar = np.arange(1, 6, .1)

x = ar
y = np.sin(ar)
plt.plot(x, y, label='sin', linestyle='--')
plt.plot(x, np.cos(ar), label='cos', linestyle=':')
#plt.plot(x, np.tan(ar), label='tan', linestyle='-.')
plt.legend()
#plt.savefig('tri.png')
plt.show()
