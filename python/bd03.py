import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print('Data Shape :', boston.data.shape)
x_room = boston.data[:, 5]
y = boston.target
print('X Shape: ', x_room.shape)
print('Y Shape', y.shape)

plt.figure()
plt.scatter(x_room, y)
plt.xlabel("rooms")
plt.ylabel("price")
plt.show()

x_room = x_room.reshape(-1,1)
y = y.reshape(-1,1)

testing = np.linspace(min(x_room), max(x_room)).reshape(-1,1)

regression = LinearRegression()
regression.fit(x_room, y)
y_pred = regression.predict(testing)

plt.figure(figsize=(10,5))
plt.scatter(x_room, y)
plt.plot(testing, y_pred, color='red', Linewidth=3)
plt.xlabel('rooms')
plt.ylabel('price')
plt.show()
