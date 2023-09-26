import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def function_3(x,y):
    return x**2+y**2
x_3=np.arange(-5,5,0.25)
y_3=np.arange(-5,5,0.25)

fig = plt.figure()
ax = fig.gca(projection='3d')

X,Y = np.meshgrid(x_3,y_3)
Z = function_3(X,Y)

surf = ax.plot_surface(X,Y,Z,cmap='coolwarm',linewidth=0,antialiased=False)
wire = ax.plot_wireframe(X,Y,Z,color='r',linewidth=0.1)
fig.colorbar(surf,shrink=0.5,aspect=5)
fig.tight_layout()
plt.show()