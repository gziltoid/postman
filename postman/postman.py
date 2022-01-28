#!/usr/bin/env python3
from collections import namedtuple
from itertools import permutations


Point = namedtuple('Point', 'x y')
points = (Point(0, 2), Point(2, 5), Point(5, 2), Point(6, 6), Point(8, 3))
PATHS_NUMBER = 24  # (n - 1)! -> (5 - 1)! = 4! = 24


def get_distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


def get_full_path_distance(path):
    return get_distance(points[0], points[path[0]]) + \
        get_distance(points[path[0]], points[path[1]]) + \
        get_distance(points[path[1]], points[path[2]]) + \
        get_distance(points[path[2]], points[path[3]]) + \
        get_distance(points[path[3]], points[0])


paths = [p for p in permutations(range(1, 5)) if p[0] <= p[-1]]
distances = [get_full_path_distance(path) for path in paths]
print(min(distances))
