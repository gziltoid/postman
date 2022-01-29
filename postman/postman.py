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


def format_result(points, path, path_length):
    full_path = [0, *path, 0]
    s = f'({points[0].x}, {points[0].y})'
    total_length = 0
    for p1, p2 in zip(full_path, full_path[1:]):
        total_length += get_distance(points[p1], points[p2])
        s += f' -> ({points[p2].x}, {points[p2].y})[{total_length}]'
    s += f' = {path_length}'
    return s


if __name__ == '__main__':
    points = (Point(0, 2), Point(2, 5), Point(5, 2), Point(6, 6), Point(8, 3))

    paths = [p for p in permutations(range(1, 5)) if p[0] <= p[-1]]
    paths_lengths = [get_path_length(points, path) for path in paths]
    min_path_length = min(paths_lengths)
    min_path_index = paths_lengths.index(min_path_length)
    min_path = paths[min_path_index]
    print(format_result(points, min_path, min_path_length))
