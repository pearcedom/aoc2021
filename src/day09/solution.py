from math import prod

def is_lowpoint(i, j, d):
    return all(d[(i, j)] < d[k] for k in adjacent(i, j))

def adjacent(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def find_low_points(d, h, w):
    return {(i, j): d[i, j] for i in range(1, h+1) for j in range(1, w+1)
        if is_lowpoint(i, j, d)}

def pool(i, j, d, v = None):
    if d[(i, j)] >= 9 or (i, j) in v:
        return set()
    else:
        cur = set([(i, j)])
        return cur | set(k for c in adjacent(i, j) for k in pool(*c, d, v | cur))

if __name__ == "__main__":
    with open('src/day09/example.txt') as f:
        ls = f.read().splitlines()
        h, w = len(ls), len(ls[0])
        d = {(i, j): 19 for i in range(h+2) for j in range(w+2)}
        for i, j in enumerate(lines):
            for k, l in enumerate(j):
                d[i+1, k+1] = int(l)

    low_points = find_low_points(d, h, w)
    bins = [pool(i, j, d, set()) for i, j in low_points]

    print("Part1:", sum(i+1 for i in low_points.values()))
    print("Part2:", prod(sorted(len(i) for i in bins)[-3:]))
