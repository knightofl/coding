import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


x = np.arange(0, np.radians(360), 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x), cos(x)')
plt.title('sin, cos')
plt.show()


x = np.arange(-180, 180)
y1 = np.sin(np.radians(x))
y2 = np.cos(np.radians(x))
plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')
plt.legend()
plt.axvline(x=0, color='y', linestyle='dotted')
plt.axhline(y=0, color='y', linestyle='dotted')
plt.xlabel('x degree')
plt.ylabel('sin(x), cos(x)')
plt.title('sin, cos')
plt.show()


x = np.arange(-4, 4.1, 0.2)
y = x**2
plt.plot(x,y, color='r')
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.show()


x = np.arange(-2, 6.1, 0.2)
y = (x-2)**2 + 4
plt.plot(x,y, color='r')
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.show()


x = np.arange(-1, 5, 0.1)
y = np.e**x
plt.plot(x,y, label='e**x')
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.legend()
plt.show()


x = np.arange(0.01, 2, 0.01)
y1 = np.log(x)
y2 = -np.log(x)
plt.plot(x,y1, label='log(x)')
plt.plot(x,y2, label='-log(x)')
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.legend()
plt.show()


x1 = np.arange(0.01, 1.2, 0.01)
y1 = -np.log(x1)
x2 = np.arange(-0.1, 1.0, 0.01) 
y2 = -np.log(1-x2)
plt.plot(x1,y1, label='-log(x)')
plt.plot(x2,y2, label='-log(1-x)')
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.legend()
plt.show()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-4, 4, 20)
print(x)
y = sigmoid(x)
plt.plot(x,y)
plt.axvline(x=0, linestyle='dotted')
plt.axhline(y=0, linestyle='dotted')
plt.show()


img = imread('./tmp/iu.jpg')
print(img.shape, img.ndim, img.dtype)
plt.imshow(img)
plt.show()
