from coordinates import Point
from coordinates import Line
from plane import Plane

with open('input.txt') as f:
    data = list(f.read().splitlines())
    data = [l.split(' -> ') for l in data]

    lines = [[point.split(',') for point in line] for line in data]
    lines = [[Point(int(x), int(y)) for x,y in l] for l in lines]
    lines = [Line(a,b) for a,b in lines]

    pt1_plane = Plane(1000)
    pt2_plane = Plane(1000)

    for line in lines:
        pt2_plane.add_line(line)

        if line.get_slope() == 0:
            pt1_plane.add_line(line)
    
    print(pt1_plane.get_num_overlaps())
    print(pt2_plane.get_num_overlaps())