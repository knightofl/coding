import numpy as np


s = np.array(50)
print(s, s.ndim, s.shape, s.dtype)

v = np.array([50])
print(v, v.ndim, v.shape, v.dtype)

m = np.array([[50], [100]])
print(m, m.ndim, m.shape, m.dtype)

v = np.array([10,20,30])
print(v)
print(np.sum(v))
print(np.sum(v, axis=0))
#print(np.sum(v, axis=1))

v = np.array([10,20,30]).reshape(3,1)
print(v)
print(np.sum(v))
print(np.sum(v, axis=0))
print(np.sum(v, axis=1))

m = np.array([[10,20,30], [30,40,50]])
print(np.sum(m, axis=0))
print(np.sum(m, axis=1))
print(np.sum(m))

v = np.diag(m)
print(v)

m = np.diag([1,2,3,4])
print(m)

m = m/4
print(m)

m = np.diag([1,2,3,4], k=1)
print(m)

m = np.diag([1,2,3,4], k=-1)
print(m)

m = np.eye(3,3)
print(m)

m = np.eye(3,3, k=1)
print(m)

m = np.eye(3,3, k=-1)
print(m)

m = np.identity(3)
print(m, m.dtype)

v = np.arange(1,10)
m = v.reshape(3,3)
print(m, m.ndim, m.shape, m.dtype)
n = np.dot(m, np.identity(3))
print(n, n.ndim, n.shape, n.dtype)

print(n.flatten())