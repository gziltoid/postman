#!/usr/bin/env python3
from functools import partial
from itertools import permutations
from typing import Tuple
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def get_distance(p1: Point, p2: Point) -> float:
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


def get_path_length(points: list[Point], path: list[int]) -> float:
    total_length = 0
    for i1, i2 in zip(path, path[1:]):
        total_length += get_distance(points[i1], points[i2])
    return total_length


def format_result(points: list[Point], path: list[int]) -> str:
    """This function duplicates some of the `get_path_length` functionality to avoid creating
    too many unused objects - it's faster to calculate the running sum of the distances again."""
    total_length = 0
    result = f"({points[0].x}, {points[0].y})"
    for i1, i2 in zip(path, path[1:]):
        total_length += get_distance(points[i1], points[i2])
        result += f" -> ({points[i2].x}, {points[i2].y})[{total_length}]"
    result += f" = {total_length}"
    return result


def get_unique_paths(points: list[Point]) -> list[Tuple]:
    """Since the permutations contain unique integers, we can filter them out by discarding
    the reversed ones via comparing the first and the last element of each permutation."""
    return [
        (0, *perm, 0)
        for perm in permutations(range(1, len(points)))
        if perm[0] <= perm[-1]
    ]


if __name__ == "__main__":
    points = (Point(0, 2), Point(2, 5), Point(5, 2), Point(6, 6), Point(8, 3))
    min_path = min(get_unique_paths(points), key=partial(get_path_length, points))

    print(format_result(points, min_path))
