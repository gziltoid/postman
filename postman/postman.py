#!/usr/bin/env python3
from collections import namedtuple
from itertools import permutations


Point = namedtuple('Point', 'x y')


def get_distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


def get_path_length(points, path):
    full_path = [0, *path, 0]
    total_length = 0
    for p1, p2 in zip(full_path, full_path[1:]):
        total_length += get_distance(points[p1], points[p2])
    return total_length


if __name__ == '__main__':
    points = (Point(0, 2), Point(2, 5), Point(5, 2), Point(6, 6), Point(8, 3))

    paths = (p for p in permutations(range(1, 5)) if p[0] <= p[-1])
    path_lengths = (get_path_length(points, path) for path in paths)
    min_path_length = min(path_lengths)
    print(min_path_length)
