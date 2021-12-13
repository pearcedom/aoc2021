def fold(cs, axis, line):
    if axis == 'y':
        cs = set((j, i - 2*(i-line) if i > line else i) for j, i in cs)
    elif axis == 'x':
        cs = set((j - 2*(j-line) if j > line else j, i) for j, i in cs)
    return cs

def decode(cs):
    cs = sorted(cs, key = lambda x: (x[1], x[0]))
    h, w = max(cs, key = lambda x: (x[1], x[0]))[1], max(cs)[0]
    out = ["".join(['█' if (j, i) in cs else ' ' for j in range(w+1)])
        for i in range(h+1)]
    return "\n".join(out)

if __name__ == '__main__':
    with open("src/day13/input.txt") as f:
        cs, folds = f.read().strip().split('\n\n')
        cs = set(tuple(int(j) for j in i.split(',')) for i in cs.split('\n'))
        folds = [tuple(i[11:].split('=')) for i in folds.split('\n')]

    axis, line = folds[0]
    print("Part1:", len(fold(cs, axis, int(line))))

    for axis, line in folds:
        cs = fold(cs, axis, int(line))
    print("Part2:")
    print(decode(cs))
