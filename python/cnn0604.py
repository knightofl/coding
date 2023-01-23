import numpy as np


m1 = np.array([[1,2,3], [4,5,6]])
m2 = np.array([[10,20,30], [40,50,60]])

print(m1+m2)
print(np.add(m1,m2))

print(m1-m2)
print(np.subtract(m1,m2))

print(m1*m2)
print(np.multiply(m1,m2))

print(m1/m2)
print(np.divide(m1,m2))

print(m1+10)
print(m2-10)
print(m1*5)
print(m2/5)

