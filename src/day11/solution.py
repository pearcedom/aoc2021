import numpy as np

def adj(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1),
            (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]

def flash(d):
    m = d.copy()
    flashed = m > float('inf')
    to_inc = zip(*np.where(d >= 0))

    while to_inc:
        for i in to_inc:
            m[i] += 1
        flashing = zip(*np.where((m > 9) & ~flashed))
        to_inc = [j for i in flashing for j in adjacent(*i)]
        flashed |= (m > 9)

    n_flashes = sum(sum(m > 9))
    m[m > 9] = 0
    return m, n_flashes

def flash_until(d, n):
    n_flashes = 0
    for i in range(n):
        d, n_more = flash(d)
        n_flashes += n_more
    return n_flashes

def synchronize(d):
    n, n_flashes, sq = 0, 0, (d.shape[0]-2)**2
    while n_flashes != sq:
        d, n_flashes = flash(d)
        n += 1
    return n

if __name__ == "__main__":
    with open('src/day11/input.txt') as f:
        d = np.pad(np.genfromtxt(f, delimiter=1), 1, constant_values = float('-inf'))

    print("Part1:", flash_until(d, 100))
    print("Part2:", synchronize(d))
