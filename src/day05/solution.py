from collections import namedtuple, defaultdict
from itertools import cycle

Point = namedtuple("Point", "x y")
Line = namedtuple("Line", "v w")

def to_line(p1, p2):
    xs = range(p1.x, p2.x+1) if p1.x < p2.x else range(p1.x, p2.x-1, -1)
    ys = range(p1.y, p2.y+1) if p1.y < p2.y else range(p1.y, p2.y-1, -1)
    if len(xs) == 1:
        xs = cycle(xs)
    elif len(ys) == 1:
        ys = cycle(ys)
    return [Point(x, y) for x, y in zip(xs, ys)]

def is_straight(p1, p2):
    return p1.x == p2.x or p1.y == p2.y

def find_overlaps(lines):
    d = defaultdict(lambda: 0)
    for i in lines:
        for j in i:
            d[j] += 1
    return len({(i, j) for i, j in d.items() if j >= 2})

if __name__ == "__main__":
    with open("src/day05/input.txt") as f:
        readin = f.read().strip().split('\n')
        x = [[Point(*[int(k) for k in j.split(',')]) for j in i.split(' -> ')] for i in readin]

    print("Part1:", find_overlaps([to_line(*i) for i in x if is_straight(*i)]))
    print("Part2:", find_overlaps([to_line(*i) for i in x]))
