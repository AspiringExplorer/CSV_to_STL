import pyvoro
object = pyvoro.compute_voronoi(
  [[1.0, 2.0, 3.0], [4.0, 5.5, 6.0]], # point positions
  [[0.0, 10.0], [0.0, 10.0], [0.0, 10.0]], # limits
  2.0, # block size
  radii=[1.3, 1.4] # particle radii -- optional, and keyword-compatible arg.
)
print(type(object))
