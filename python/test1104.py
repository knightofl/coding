import numpy as np

# 정렬
ex1 = np.array([3,2,5,9,7,8,4])
ex2 = np.array([3,2,5,9,7,8,4])
ex3 = np.array([[2,5,4], [3,1,6]])

ex1.sort()
print(ex1)

np.sort(ex2)
print(ex2)

print(np.sort(ex2))
print(np.sort(ex2)[::-1])

print(np.sort(ex3, axis=0))
print(np.sort(ex3, axis=1))

print(ex2)
print(np.argsort(ex2))
print(ex2[np.argsort(ex2)])
print(ex2[np.argsort(ex2)[::-1]])

# 선형대수
ex4 = np.array([[2,5,3], [6,7,3]])
ex5 = np.array([[6,4], [2,3], [5,3]])

print(ex4)
print(ex5)
print(np.dot(ex4, ex5))
print(np.dot(ex4, ex5).transpose())
