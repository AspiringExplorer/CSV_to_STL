import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.spatial import Delaunay
from stl import mesh

# u, v are parameterisation variables
u = np.array([0,0,0.5,1,1])
v = np.array([0,1,0.5,0,1])

x = u
y = v
z = np.array([0,0,1,0,0])

# Triangulate parameter space to determine the triangles
#tri = mtri.Triangulation(u, v)
tri = Delaunay(np.array([u,v]).T)

print(tri)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# The triangles in parameter space determine which x, y, z points are
# connected by an edge
#ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap=plt.cm.Spectral)


plt.show()


mesh.normals

cube = mesh.Mesh(np.zeros(tri.shape[0], dtype=mesh.Mesh.dtype))

cube.save('test.stl')
