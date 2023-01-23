import numpy as np

a = np.arange(10)
print(a, type(a), a.shape, a.ndim, a.dtype)

b = np.array([1, 2, 4])
print(b, type(b), b.shape, b.ndim, b.dtype)

c = np.array([[2, 3, 4], [1, 2, 3]])
print(c, type(c), c.shape, c.ndim, c.dtype)

d = np.array([1.1, 2, 4])
print(d, type(d), d.shape, d.ndim, d.dtype)

e = c.astype('int8')
print(e, type(e), e.shape, e.ndim, e.dtype)

print(c.sum())
print(c.sum(axis=0))
print(c.sum(axis=1))

f = np.zeros((3, 2), dtype='int32')
print(f)

g = np.ones((2, 3), dtype='float32')
print(g)

h = g.reshape(3, 2)
print(h)

print(a.reshape(-1, 5))
print(a.reshape(2, -1))

print(a.reshape(1, -1))
print(a.reshape(-1, 1))

# 팬시 인덱싱
print(c)
print(c[[0], [1,2]])
print(c[[1], [1,2]])
print(c[[0,1], [1,2]])

# 불리언 인덱싱
print(a)
i = a[a%2 == 0]
print(i)
