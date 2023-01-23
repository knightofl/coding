import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identify_function(x):
    return x

def forward(x, weight, bias):
    return np.dot(x, weight) + bias
    

network = {}
network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
network['B1'] = np.array([0.1, 0.2, 0.3])
network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
network['B2'] = np.array([0.1, 0.2])
network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
network['B3'] = np.array([0.1, 0.2])

x = np.array([1.0, 0.5])

a = forward(x, network['W1'], network['B1'])
z = sigmoid(a)

print(z.shape, network['W2'].shape)
a = forward(z, network['W2'], network['B2'])
z = sigmoid(a)

a = forward(z, network['W3'], network['B3'])
z = identify_function(a)

print(z)
