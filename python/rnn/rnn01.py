import numpy as np

x = np.array([[1,2,3], [4,5,6]])
w = np.array([[0,1,2], [3,4,5]])

print(x, x.shape, x.ndim)
print(w, w.shape, w.ndim)

print(x+w)
print(x*w)

print(x * 10)

y = np.array([1,2,3])
print(x*y)


a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a, b)) # 벡터의 내적
print(np.cross(a, b)) # 벡터의 외적

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print(a, '\n', b)
print(np.dot(a, b)) # 행렬의 곱
print(np.matmul(a, b)) # 행렬의 곱

