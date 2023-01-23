import numpy as np
import matplotlib.pyplot as plt

'''
- color : https://matplotlib.org/api/colors_api.html
- markers : https://matplotlib.org/api/markers_api.html
'''


plt.figure()
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')
plt.show()

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.ylabel('some numbers')
plt.show()

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g-o')
plt.ylabel('some numbers')
plt.show()

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
plt.xlim([0, 5])
plt.ylim([0, 20])
plt.ylabel('some numbers')
plt.show()

t = np.arange(0., 5., 0.2)
plt.figure(figsize=(8,4))
plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g^')
plt.title('Plot Test')
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.show()

t = np.arange(0., 5., 0.2)
plt.figure(figsize=(8,4))
plt.plot(t, t, 'r--', label='a')
plt.plot(t, t**2, 'bs', label='b')
plt.plot(t, t**3, 'g^', label='c')
plt.title('Plot Test')
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.legend()
#plt.savefig('test.png', dpi=100)
plt.show()

