# # Generate random data points
#
# from random import randint
# n = 254
# N = 10000
# points = {(randint(1, n), randint(1, n), randint(1, n)) for i in range(N)}
# while len(points) < N:
#     points |= {(randint(1, n), randint(1, n), randint(1, n))}
# points = list(list(x) for x in points)
#
# #print(points)

# Points at the corners of a unit cube
points=[
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1], # first attempts at a cube ends here
 ]

# # Points at the corners of a unit cube and points at the center of faces and
# # at midpoint of all edges, generates interesting resluts
# points=[
#     [0,0,0],
#     [0,0,.5],
#     [0,0,1],
#     [0,.5,0],
#     [0,.5,.5],
#     [0,.5,1],
#     [0,1,0],
#     [0,1,.5],
#     [0,1,1],
#     [.5,0,0],
#     [.5,0,.5],
#     [.5,0,1],
#     [.5,.5,0],
#     [.5,.5,.5],
#     [.5,.5,1],
#     [.5,1,0],
#     [.5,1,.5],
#     [.5,1,1],
#     [1,0,0],
#     [1,0,.5],
#     [1,0,1],
#     [3,.5,0],
#     [1,.5,.5],
#     [1,.5,1],
#     [1,1,0],
#     [1,1,.5],
#     [1,1,3],
# ]

# This StackOverflow link might be worth looking into:
#
# http://stackoverflow.com/questions/26434726/return-surface-triangle-of-3d-scipy-spatial-delaunay



import pyvoro
#for use with Python3, use the following:
#https://github.com/wackywendell/pyvoro/tree/python3

import numpy as np
from stl import mesh

# Remove duplicate points from list of points
points = sorted(points)
points = [points[i] for i in range(len(points)) if i == 0 or points[i] != points[i-1]]

object = pyvoro.compute_voronoi(
  points, # point positions
  [[0.0, 1.01], [0.0, 1.01], [0.0, 1.01]], # limits
  1, # block size
  radii=[10, 10] # particle radii -- optional, and keyword-compatible arg.
)
print(object[1])
thing = object[1]
print('\n')
print(thing['vertices'])
print('\n')
print(thing['adjacency'])

# Define the 8 vertices of the cube
vertices = thing['vertices']
vertices = np.array( vertices )
print(vertices)
# Define the 12 triangles composing the cube
faces = thing['adjacency']
faces = np.array( faces )
print(faces)

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]

# Write the mesh to file "cube.stl"
cube.save('object.stl')
