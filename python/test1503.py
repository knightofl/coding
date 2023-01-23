import numpy as np

a = np.array([1, 2, 4])
print(a, type(a), a.shape, a.ndim)

b = np.array([[1, 2, 3], [3, 4, 5]])
print(b, type(b), b.shape, b.ndim)

c = np.array([[[1], [2]], [[3], [4]]])
print(c, type(c), c.shape, c.ndim)
