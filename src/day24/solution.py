import re
from functools import cache

def mul(x, y):
    return x * y

def add(x, y):
    return x + y

def mod(x, y):
    return x % y

def div(x, y):
    return x // y

def eql(x, y):
    return int(x == y)

@cache
def step(z, w, block):
    x = y = 0
    for i in block:
        if i.startswith('w'):
            w = eval(i[4:])
        elif i.startswith('x'):
            x = eval(i[4:])
        elif i.startswith('y'):
            y = eval(i[4:])
        elif i.startswith('z'):
            z = eval(i[4:])
    return z

@cache
def r(z, blocks):
    if not blocks:
        return [(z == 0, "")]
    res = []
    for w in range(1, 10):
        zw = step(z, w, blocks[0])
        if zw < 10000000:
            res += [(i, str(w) + j) for i, j in r(zw, blocks[1:]) if i]
    return res

with open('src/day24/input.txt') as f:
    cmds = [re.sub("(\w) (.+)", "\\1(\\2)", i) for i in f.read().splitlines()]
    cmds = [re.sub(" ", ", ", i) for i in cmds]
    cmds = [re.sub("(.+)\\((\w)(.*)\\)", "\\2 = \\1(\\2\\3)", i) for i in cmds]
    cmds = [re.sub("(.*)(inp)\\((.*)\\)", "\\1\\2()", i) for i in cmds]

blocks = tuple(tuple(cmds[i+1:i+18]) for i, j in enumerate(cmds) if 'inp' in j)

out = r(0, blocks)

z = 0
ans = "94992994195998"

w, ans = ans[0], ans[1:]
w = int(w)
block, blocks = blocks[0], blocks[1:]
z = step(z, w, block)
ans, z
