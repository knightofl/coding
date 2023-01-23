import numpy as np
import matplotlib.pyplot as plt


fig, splts = plt.subplots(2)
splts[0].plot([10,11,12,13], [9,8,7,6])
splts[1].plot([5,6,7,8], [9,7,8,6])
plt.show()


fig, splts = plt.subplots(1,2)
splts[0].plot([10,11,12,13], [9,8,7,6])
splts[1].plot([5,6,7,8], [9,7,8,6])
plt.show()


fig, splts = plt.subplots(2,2)
splts[0,0].plot([1,2,3,4], [10, 20, 15, 25])
splts[0,1].plot(np.random.randn(50).cumsum(), 'k--')
splts[1,0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
splts[1,1].scatter(np.arange(100), np.arange(100) + 3*np.random.randn(100))
plt.show()


fig, splts = plt.subplots(2,2, sharex=True, sharey=True)

for i in range(2):
    for j in range(2):
        splts[i,j].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
plt.show()


fig, splts = plt.subplots(1,1)
splts.plot([10,20,30,40], label='data1')
splts.plot([9,15,21,27], label='data2')
plt.legend(loc='best')
plt.show()

