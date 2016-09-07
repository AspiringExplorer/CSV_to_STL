import csv
import pyvoro
from stl import mesh

with open("./points.csv") as f:
    records = list(csv.reader(f))

points = [
    dict(
        zip(
            records[0],
            map(float, record)
        )
    )
    for record
    in records[1:]
]

vecs = [
    [point[k] for k in "lon lat".split(" ")]
    for point
    in points
]
transposed = zip(*vecs)
borders = zip(
    *[
        map(f, transposed)
        for f
        in [min, max]
    ]
)[:2]
world_diameter = (
    (
        borders[0][1] - borders[0][0]
    ) ** 2 + (
        borders[1][1] - borders[1][0]
    ) ** 2
) ** .5
cells = pyvoro.compute_2d_voronoi(vecs, [[least-1, most+1] for least, most in borders], world_diameter, z_height=world_diameter)

assert len(points) == len(cells)

def square_distance_to_cell(point, cell):
    dlon = point["lon"] - cell["original"][0]
    dlat = point["lat"] - cell["original"][1]
    return dlon ** 2 + dlat ** 2

def compare_cell_distances(point, a, b):
    delta = square_distance_to_cell(point, a) - square_distance_to_cell(point, b)
    if delta > 0: return 1
    if delta < 0: return -1
    return 0

for point in points:
    point["cell"] = list(
        sorted(
            cells,
            lambda a, b: compare_cell_distances(point, a, b)
        )
    )[0]
    point["cell"]["point"] = point

triangles = []
for point in points:
    point["edges"] = []
    for edge in point["cell"]["faces"]:
        face = {
            "neighbor": cells[edge["adjacent_cell"]],
            "vertices": [
                {
                    "point": point["cell"]["vertices"][i],
                    "index": i,
                    "neighbor": [
                        j
                        for j, neighbor
                        in enumerate(point["cell"]["faces"])
                        if neighbor is not edge and i in neighbor["vertices"]
                    ][0],
                }
                for i
                in edge["vertices"]
            ],
            "center": point,
        }
        point["edges"].append(face)
        triangles.append(face)
    for edge in point["edges"]:
        pass

# TODO: find common vertices
#  and use them to sample the mean heights of the cells they touch
#  then generate appropriate triangles, two per directed edge
