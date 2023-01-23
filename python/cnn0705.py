import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-1, 5, 0.1)
y = x**2 * np.exp(-x)
plt.plot(x, y)
plt.axvline(x=0, color='y', linestyle='dotted')
plt.axhline(y=0, color='y', linestyle='dotted', label='x**2 * np.exp(-x)')
plt.legend(loc='best')
plt.show()


x = np.arange(-5, 5, 0.01)
y = x**3 / (x**2 - 1)
plt.scatter(x, y)
plt.ylim(-6, 6)
plt.axvline(x=0, color='y', linestyle='dotted')
plt.axhline(y=0, color='y', linestyle='dotted', label='x**3 / (x**2 - 1)')
plt.show()


def f(x, y):
    return (x + y)**2

x = np.arange(-5, 5.1, 0.1)
y = np.arange(-5, 5.1, 0.1)

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
