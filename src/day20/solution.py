def pad_range(d, dim):
    x = [i for i, _ in d] if dim == 1 else [j for _, j in d] if dim == 2 else []
    return range(min(x)-1, max(x)+2)

def adjacent(i, j):
    return [
        (i-1, j-1), (i-1, j+0), (i-1, j+1),
        (i+0, j-1), (i+0, j+0), (i+0, j+1),
        (i+1, j-1), (i+1, j+0), (i+1, j+1),
        ]

def enhance(d, iteration):
    nxt = d.copy()
    for row in pad_range(d, dim = 1):
        for col in pad_range(d, dim = 2):
            n = []
            for i, j in adjacent(row, col):
                try:
                    n.append(d[i, j])
                except KeyError:
                    n.append(('0', '1')[iteration % 2])
            nxt[row, col] = algorithm[int("".join(n), 2)]
    return nxt

def enhance_until(d, until):
    for iteration in range(until):
        d = enhance(d, iteration)
    return d

with open('src/day20/input.txt') as f:
    algorithm, img = f.read().strip().split('\n\n')
    algorithm = algorithm.replace('#', '1').replace('.', '0')
    img = img.split('\n')
    d = {}
    for i in range(len(img)):
        for j in range(len(img[0])):
            d[i, j] = '1' if img[i][j] == '#' else '0'

    print("Part1:", sum(int(i) for i in enhance_until(d, 2).values()))
    print("Part2:", sum(int(i) for i in enhance_until(d, 50).values()))
