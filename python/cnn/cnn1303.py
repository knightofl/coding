import numpy as np
import pickle
from tensorflow.keras.datasets.mnist import load_data


def sigmoid(x):
    return 1 / (1 + np.exp(-x))   

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x -= np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    x -= np.max(x)
    return np.exp(x) / np.sum(np.exp(x))

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


(x_train, t_train), (x_test, t_test) = load_data()
x_train = x_train.reshape(-1, 28*28) / 255.0
x_test = x_test.reshape(-1, 28*28) / 255.0
#t_train = np.eye(10)[t_train]
#t_test = np.eye(10)[t_test]

with open("./scratch1/ch03/sample_weight.pkl", 'rb') as f:
    network = pickle.load(f)


test_size = x_test.shape[0]
batch_size = 100
accuracy = 0

for i,b in enumerate(range(0, test_size, batch_size)):
    correct = 0
    x_batch = x_test[b:b+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    correct = np.sum(p == t_test[b:b+batch_size])
    accuracy += correct
    print(f'{i+1} {b} Correct: {correct} {accuracy}')
    
print(f'Accuracy: {float(accuracy) / test_size}')

accuracy = 0
for i in range(test_size):
    if np.argmax(predict(network, x_test[i])) == t_test[i]:
        accuracy += 1
print(f'Accuracy: {float(accuracy) / test_size}')

