#!/usr/bin/env python3


from collections import namedtuple


points = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))
PATHS_NUMBER = 24  # (n - 1)! -> (5 - 1)! = 4! = 24

Point = namedtuple('Point', 'x y')


def get_distance(p1, p2):
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
