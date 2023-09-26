import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def fun(x, y):
    return x**2 + y**2

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)

print(fun(x, y))

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y = np.meshgrid(x, y)
Z = fun(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)
wire = ax.plot_wireframe(X, Y, Z, color='r', linewidth=0.1)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.tight_layout()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

