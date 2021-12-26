def can_move(c, d, h, w):
    i, j = c
    if d[i, j] == '>':
        return d[i, j+1 if j < w else 0] == '.'
    if d[i, j] == 'v':
        return d[i+1 if i < h else 0, j] == '.'
    else:
        return False

def move(d, h, w):
    d = d.copy()
    for herd in ['>', 'v']:
        moves = []
        for c in d:
            if d[c] == herd and can_move(c, d, h, w):
                moves += [c]
        for i, j in moves:
            if herd == '>':
                d[i, j+1 if j < w else 0] = d[i, j]
                d[i, j] = '.'
            elif herd == 'v':
                d[i+1 if i < h else 0, j] = d[i, j]
                d[i, j] = '.'
    return d

def equilibrate(d, h, w):
    prev = {}
    n = 0
    while d != prev:
        d, prev = move(d, h, w), d
        n+=1
    return n

d = {}
with open('src/day25/input.txt') as f:
    for i, line in enumerate(f.read().splitlines()):
        for j, char in enumerate(line):
            d[i, j] = char
    h, w = i, j

    print("Part1:", equilibrate(d, h, w))
