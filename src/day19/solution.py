reorders = [
    (0, 1, 2), (0, 2, 1), (0, 1, 2), (0, 2, 1), (0, 1, 2), (0, 2, 1), (0, 1, 2),
    (0, 2, 1), (1, 2, 0), (1, 0, 2), (1, 2, 0), (1, 0, 2), (1, 2, 0), (1, 0, 2),
    (1, 2, 0), (1, 0, 2), (2, 0, 1), (2, 1, 0), (2, 0, 1), (2, 1, 0), (2, 0, 1),
    (2, 1, 0), (2, 0, 1), (2, 1, 0)
]

signs = [
    (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1),
    (-1, -1, -1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1), (-1, -1, 1), (-1, 1, 1),
    (-1, 1, -1), (-1, -1, -1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (1, 1, -1), (-1, -1, 1),
    (-1, 1, 1), (-1, 1, -1), (-1, -1, -1)
]

def dist(x, y):
    return tuple(j-i for i, j in zip(x, y))

def pairwise_dists(xs):
    return [(i, [dist(i, j) for j in xs if i != j]) for i in xs]

def find_mate(beacons, master, scanners):
        beacon, beacons = beacons[0], beacons[1:]
        master_dists = pairwise_dists(master)
        for reshape in zip(reorders, signs):
            rotation = [tuple(j*cs[i] for i, j in zip(*reshape)) for cs in beacon]
            rotation_dists = pairwise_dists(rotation)
            for i in master_dists:
                for j in rotation_dists:
                    if len(set(i[1]) & set(j[1])) >= 11:
                        di, dj, dk = [i-j for i, j in zip(i[0], j[0])]
                        master |= set((i+di, j+dj, k+dk) for i, j, k in rotation)
                        scanners.append((di, dj, dk))
                        return beacons, master, scanners
        else:
            return beacons + [beacon], master, scanners

def pairwise_hamming(xs):
    return max([sum(abs(j-i) for i, j in zip(x, y)) for x in xs for y in xs])

if __name__ == '__main__':
    with open('src/day19/input.txt') as f:
        beacons = [i.split('\n')[1:] for i in f.read().strip().split('\n\n')]
        beacons = [[tuple(int(k) for k in j.split(',')) for j in i] for i in beacons]

    master, beacons = set(beacons[0]), beacons[1:]
    scanners = [(0, 0, 0)]
    while beacons:
        beacons, master, scanners = find_mate(beacons, master, scanners)

    print("Part1:", len(master))
    print("Part2:", pairwise_hamming(scanners))
