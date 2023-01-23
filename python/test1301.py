import matplotlib.pyplot as plt

even = [1, 2, 3, 4]
plt.plot(even, even)
plt.plot(even, (lambda x: [i**2 for i in x])(even))
plt.show()
