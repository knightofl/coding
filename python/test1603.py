import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    max = np.max(x)
    ex = np.exp(x - max)
    sum = np.sum(ex)
    return ex / sum

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
z = softmax(a)
print(z)

# ex
def softsig(x):
    sig = sigmoid(x)
    sum = np.sum(sig)
    return sig / sum

b = np.array([0.3, 2.9, 4.0])
print(softmax(b))
print(softsig(b))
