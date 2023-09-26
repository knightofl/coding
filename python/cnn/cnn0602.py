import numpy as np


arr1 = np.zeros(5)
print(arr1, arr1.ndim, arr1.shape, arr1.dtype)

arr2 = np.zeros((4,5))
print(arr2, arr2.ndim, arr2.shape, arr2.dtype)

arr3 = np.ones(5)
print(arr3, arr3.ndim, arr3.shape, arr3.dtype)

arr4 = np.ones((4,5))
print(arr4, arr4.ndim, arr4.shape, arr4.dtype)

arr5 = np.full(2,5)
print(arr5, arr5.ndim, arr5.shape, arr5.dtype)

arr6 = np.full((2,3), 5)
print(arr6, arr6.ndim, arr6.shape, arr6.dtype)

arr7 = arr4.reshape(-1,2)
print(arr7, arr7.ndim, arr7.shape, arr7.dtype)

arr8 = np.zeros_like(arr4)
print(arr8, arr8.ndim, arr8.shape, arr8.dtype)
