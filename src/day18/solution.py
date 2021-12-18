from collections import namedtuple
from math import floor, ceil
from functools import reduce

Num = namedtuple('Num', ['x', 'depth'])
Num.__repr__ = lambda x: f"{x.x}{['.', '∶', '∴', '∷', '*'][x.depth-1]}"

def flatNums(x, depth = 0):
    out = []
    for i in x:
        if isinstance(i, int):
            out.append(Num(i, depth + 1))
        else:
            out.extend(flatNums(i, depth + 1))
    return out

def add(x, y):
    return simplify([Num(i.x, i.depth+1) for i in x + y])

def simplify(x):
    nxt = reducify(x)
    while x != nxt:
        x, nxt = nxt, reducify(nxt)
    return x

def reducify(x):
    for i, lnum in enumerate(x):
        if lnum.depth > 4:
            if i > 0:
                ladj = x[i-1]
                x[i-1] = Num(ladj.x + lnum.x, ladj.depth)
            if i+2 < len(x):
                rnum = x[i+1]
                radj = x[i+2]
                x[i+2] = Num(radj.x + rnum.x, radj.depth)
            x = x[0:i] + [Num(0, lnum.depth - 1)] + x[i+2:]
            return x
    for i, lnum in enumerate(x):
        if lnum.x >= 10:
            div = lnum.x / 2
            depth = lnum.depth
            x = x[0:i] + [Num(floor(div), depth+1), Num(ceil(div), depth+1)] + x[i+1:]
            return x
    return x

def magnitude(x):
    while len(x) > 1:
        for i, l in enumerate(x[0:-1]):
            r = x[i+1]
            if l.depth == r.depth:
                x[i+1] = Num(3*l.x + 2*r.x, l.depth-1)
                x = x[0:i] + x[i+1:]
                break
    return x[0].x

def sum_sf(xs):
    out = reduce(lambda a, b: add(a, flatNums(b)), xs[1:], flatNums(xs[0]))
    return magnitude(out)

def max_pw_sum(xs):
    return max(max(sum_sf([i, j]), sum_sf([j, i])) for i in xs for j in xs if i != j)

if __name__ == '__main__':
    with open('src/day18/input.txt') as f:
        xs = [eval(i) for i in f.read().splitlines()]

    print('Part1:', sum_sf(xs))
    print('Part2:', max_pw_sum(xs))
