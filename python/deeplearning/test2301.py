# test1402
import matplotlib.pyplot as  plt
import numpy as np
from tensorflow import keras

data = np.array([
    [0.72,0.82,-1],
    [0.91,-0.69,-1],
    [0.03,0.93,-1],
    [0.12,0.25,-1],
    [0.96,0.47,-1],
    [0.8,-0.75,-1],
    [0.46,0.98,-1],
    [0.66,0.24,-1],
    [0.72,-0.15,-1],
    [0.35,0.01,-1],
    [-0.11,0.1,1],
    [0.31,-0.96,1],
    [0.0,-0.26,1],
    [-0.43,-0.65,1],
    [0.57,-0.97,1],
    [-0.72,-0.64,1],
    [-0.25,-0.43,1],
    [-0.12,-0.9,1],
    [-0.58,0.62,1],
    [-0.77,-0.76,1]
])


plt.scatter(data[:, 0], data[:, 1], c=data[:, 2])
plt.show()

my_model = keras.Sequential()
my_model.add(keras.layers.Dense(1, activation='sigmoid', input_shape=(2,)))

optimizer = keras.optimizers.SGD(lr=0.2)
my_model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
my_model.fit(data[:, :2], data[:, 2]==1, batch_size=5, epochs=500)

#print(my_model.predict(data[:,:2]))
#print(np.round(my_model.predict(data[:,:2])))

print(my_model.layers[0].get_weights())

weight = my_model.layers[0].get_weights()[0]
bias = my_model.layers[0].get_weights()[1]
x = np.linspace(np.amin(data[:, 0]), np.amax(data[:, 0]))
#print(x)

plt.scatter(data[:, 0], data[:, 1], c=data[:, 2])
a = -weight[0] / weight[1]
b = -(weight[0]/weight[1]) / (weight[1]/bias[0])
plt.plot(x, [a*i + b for i in x], color='green')
plt.show()

