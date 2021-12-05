from collections import namedtuple, defaultdict, Counter
from itertools import cycle

Point = namedtuple("Point", "x y")

def to_line(p1, p2):
    xs = range(p1.x, p2.x+1) if p1.x < p2.x else range(p1.x, p2.x-1, -1)
    ys = range(p1.y, p2.y+1) if p1.y < p2.y else range(p1.y, p2.y-1, -1)
    xs, ys = (cycle(xs), ys) if len(xs) == 1 else (xs, cycle(ys))
    return [Point(x, y) for x, y in zip(xs, ys)]

def is_straight(p1, p2):
    return p1.x == p2.x or p1.y == p2.y

def find_overlaps(lines):
    point_counts = Counter([j for i in lines for j in i])
    return len([i for i, j in point_counts.items() if j >= 2])

if __name__ == "__main__":
    with open("src/day05/input.txt") as f:
        lines = [i.split(' -> ') for i in f.read().splitlines()]
        x = [[Point(*map(int, j.split(','))) for j in i] for i in lines]

    print("Part1:", find_overlaps([to_line(*i) for i in x if is_straight(*i)]))
    print("Part2:", find_overlaps([to_line(*i) for i in x]))
