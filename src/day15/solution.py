from bisect import insort

def adjacent(i, j, h, w):
    adj = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    return set(i for i in adj if in_bounds(*i, h, w))

def in_bounds(i, j, h, w):
    return i >= 0 and j >= 0 and i <= h and j <= w

def find_path(d):
    scores = {i: float('inf') for i in d}
    target = max(d.keys())
    cur = 0
    visited = set()
    p, c = (0, 0), []

    while p != target:

        adj = adjacent(*p, *target) - visited
        for i in adj:
            scores[i] = min(scores[i], d[i] + cur)
            insort(c, i, key = lambda x: scores[x])
        visited |= set([p])
        c = [i for i in c if i not in visited]
        p, c = c[0], c[1:]
        cur = scores[p]

    return scores[target]

with open("src/day15/input.txt") as f:
    lines = f.read().splitlines()
    d1 = dict()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            d1[i, j] = int(char)

    d2 = dict()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            d2[i, j] = int(char)
            for n in range(5):
                for m in range(5):
                    c1 = i+n*len(lines)
                    c2 = j+m*len(line)
                    value = (int(char) + n+m)
                    d2[c1, c2] = value if value <= 9 else (value + 1) % 10

print("Part1:", find_path(d1))
print("Part2:", find_path(d2))
