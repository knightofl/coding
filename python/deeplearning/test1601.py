import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identify_function(x):
    return x

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(X.shape, W1.shape, B1.shape)
A1 = np.dot(X, W1) + B1
B1 = sigmoid(A1)

print(X)
print(A1, B1) 