import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + y**2

x = np.arange(-4, 4.1, 0.5)
y = np.arange(-4, 4.1, 0.5)

fig = plt.figure()
ax = fig.gca(projection='3d')

X,Y = np.meshgrid(x,y)
Z = f(X, Y)

surf = ax.plot_surface(X,Y,Z, cmap='coolwarm', linewidth=0, antialiased=True)
wire = ax.plot_wireframe(X,Y,Z, color='r', linewidth=0.1)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.tight_layout()
plt.show()



def num_grad(f, x, y):
    h = 1e-4
    grad_x = (f(x+h, 0) - f(x-h, 0)) / (2*h)
    grad_y = (f(0, y+h) - f(0, y-h)) / (2*h)
    return np.array([grad_x, grad_y])

X, Y = np.meshgrid(x, y)

X = X.flatten()
Y = Y.flatten()

grad = num_grad(f, X, Y)

plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1], angles="xy", color="#666666") 
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

