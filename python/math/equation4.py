import numpy as np
from scipy.spatial import distance
#from scipy import linalg


s = np.array([2,3,4])
v_hat = s / np.linalg.norm(s)
print(v_hat)
v_hat = s / (s**2).sum()**0.5
print(v_hat)


print(np.zeros(5))
print(np.zeros((5,5)))


s = np.array([[3,4], [5,6], [8,10]])
print(np.linalg.matrix_rank(s))


u = np.array(((3,4),(5,6)))
v = np.array(((4,5),(6,7)))
print(u+v)
print(u*v)
print(u-v)
print(u@v)
print(np.dot(u,v))
print(np.matmul(u,v))

A = np.arange(1*2*3).reshape((1,2,3))
B1 = np.arange(1*2*3).reshape((1,2,3))
B2 = np.arange(1*3*2).reshape((1,3,2))
#print(np.dot(A,B1))
print(np.dot(A,B2))


a = np.array((1,3,5))
b = np.array((2,4,6))
print(np.cross(a,b))


print(np.linalg.norm(a))
print(np.linalg.norm(a, ord=1))
print(np.linalg.norm(a, ord=2))


print(distance.euclidean(a, b))
print(np.linalg.norm(b-a))


c = np.matrix([[1, 0, 0, 0], [2, 1, 0, 0], [3, 0, 1, 0], [4, 0, 0, 1]])
print(c)
d = np.linalg.inv(c)
print(d)
print(np.dot(c,d))


print(c.T)
print(np.transpose(c))
print(np.swapaxes(c,0,1))


e = np.array(((2,5),(4,3)))
print(e)

w, v = np.linalg.eig(e)
print(w)
print(v) #정규화