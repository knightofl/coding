import numpy as np


print(np.__version__, np.ndarray)

print(np.e)
print(np.pi)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


arr0 = np.array(10)
print(arr0, arr0.ndim, arr0.shape, arr0.dtype)

l1 = [1,2,3,4]
arr1 = np.array(l1)
print(arr1, arr1.ndim, arr1.shape, arr1.dtype)

l2 = [1.1, 2.2, 3.3, 4.4]
arr2 = np.array(l2)
print(arr2, arr2.ndim, arr2.shape, arr2.dtype)

l3 = [[1,2,3], [10,20,30], [100,200,300], [1000,2000,3000]]
arr3 = np.array(l3)
print(arr3, arr3.ndim, arr3.shape, arr3.dtype)

arr4 = np.arange(10)
print(arr4, arr4.ndim, arr4.shape, arr4.dtype)

arr5 = np.linspace(0, 1, 6)
print(arr5, arr5.ndim, arr5.shape, arr5.dtype)

arr6 = arr3[:, 1]
print(arr6, arr6.ndim, arr6.shape, arr6.dtype)

arr7 = arr3[1, :]
print(arr7, arr7.ndim, arr7.shape, arr7.dtype)

arr8 = arr3[:, np.newaxis]
print(arr8, arr8.ndim, arr8.shape, arr8.dtype)

arr9 = arr3[np.newaxis, :]
print(arr9, arr9.ndim, arr9.shape, arr9.dtype)


print(arr3.size)
print(len(arr3))

row, col = arr3.shape
for i in range(row):
    for j in range(col):
        print(f'(arr{i},{j}) : {arr3[i,j]}')

print(arr3.T)
print(np.transpose(arr3))
print(np.swapaxes(arr3, 0, 1))

arr10 = np.array([1,2,3])
print(arr10, arr10.shape, arr10.ndim)

arr11 = arr10.T
print(arr11, arr11.T.shape, arr11.T.ndim)

arr12 = arr10.reshape(-1,1)
print(arr12, arr12.shape, arr12.ndim)
