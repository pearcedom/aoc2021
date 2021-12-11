def adjacent(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1),
            (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]

def flash(d, h, w):
    m = d.copy()
    flashed = set()
    to_flash = [(i, j) for i in range(h+2) for j in range(w+2)]

    while to_flash:
        for i in to_flash:
            m[i] += 1

        to_flash = []
        for i in range(1, h+1):
            for j in range(1, w+1):
                if m[i, j] > 9 and (i, j) not in flashed:
                    to_flash += adjacent(i, j)
                    flashed |= set([(i, j)])

    n_flashes = 0
    for i in range(h+1):
        for j in range(w+1):
            if m[i, j] > 9:
                m[i, j] = 0
                n_flashes += 1

    return m, n_flashes

def flash_until(d, h, w, n):
    n_flashes = 0
    for i in range(n):
        d, n_more = flash(d, h, w)
        n_flashes += n_more
    return n_flashes

def synchronize(d, h, w):
    n, n_flashes, sq = 0, 0, h * w
    while n_flashes != sq:
        d, n_flashes = flash(d, h, w)
        n += 1
    return n

if __name__ == "__main__":
    with open('src/day11/input.txt') as f:
        lines = f.read().splitlines()
        h, w = len(lines), len(lines[0])
        d = {(i, j): float('-inf') for i in range(h+2) for j in range(w+2)}
        for i, j in enumerate(lines):
            for k, l in enumerate(j):
                d[i+1, k+1] = int(l)

    print("Part1:", flash_until(d, h, w, 100))
    print("Part2:", synchronize(d, h, w))
