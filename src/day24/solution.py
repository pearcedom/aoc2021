import re
from functools import cache

def step(z, w, zdiv, xadd, yadd):
    # Thanks reddit
    if (z%26 + xadd) != w:
        return z//zdiv*26 + w + yadd
    else:
        return z//zdiv

@cache
def f(z, zdivs, xadds, yadds):
    if not zdivs:
        return [(z == 0, "")]
    results = []
    for w in range(1, 10):
        zw = step(z, w, zdivs[0], xadds[0], yadds[0])
        if zw < 10000000:
            res = [(i, str(w) + j) for i, j in f(zw, zdivs[1:], xadds[1:], yadds[1:]) if i]
            results += res
    return results

if __name__ == '__main__':
    with open('src/day24/input.txt') as file:
        cmds = [re.sub("(\w) (.+)", "\\1(\\2)", i) for i in file.read().splitlines()]
        cmds = [re.sub(" ", ", ", i) for i in cmds]
        cmds = [re.sub("(.+)\\((\w)(.*)\\)", "\\2 = \\1(\\2\\3)", i) for i in cmds]
        cmds = [re.sub("(.*)(inp)\\((.*)\\)", "\\1\\2()", i) for i in cmds]

    inp_index = [i for i, j in enumerate(cmds) if 'inp' in j]
    zdivs = tuple(int(re.findall('\d+', cmds[i + 4])[0]) for i in inp_index)
    xadds = tuple(int(re.findall('-{0,1}\d+', cmds[i + 5])[0]) for i in inp_index)
    yadds = tuple(int(re.findall('\d+', cmds[i + 15])[0]) for i in inp_index)

    ans = f(0, zdivs, xadds, yadds)

    print("Part1:", ans[-1][1])
    print("Part2:", ans[0][1])


