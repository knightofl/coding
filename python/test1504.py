import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([7, 8])
print(np.dot(a, b))

c = np.array([[1, 2], [3, 4], [5, 6]])
d = np.array([[7], [8]])
print(np.dot(c, d))

e = np.array([1, 2])
f = np.array([[1, 3, 5], [2, 4, 6]])
print(np.dot(e,f))