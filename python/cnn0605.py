import numpy as np


m1 = np.array([[1,2], [3,4], [5,6]])
m2 = np.array([[10, 20], [30,40]])

print(m1 @ m2)
print(np.dot(m1,m2)) # 행렬 곱
print(np.matmul(m1,m2)) # 행렬 곱


v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print(v1,v2)
print(np.dot(v1,v2)) # 벡터 내적
print(np.cross(v1,v2)) # 벡터 외적


m1 = np.arange(2*3*4).reshape((2,3,4))
m2 = np.arange(2*4*3).reshape((2,4,3))
print(np.dot(m1,m2).shape)
print(np.matmul(m1,m2).shape)

