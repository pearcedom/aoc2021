from collections import defaultdict

def input2dict(input):
    d = defaultdict(set)
    for i in input.split('\n'):
        key, value = i.split('-')
        d[key] |= set([value])
        d[value] |= set([key])
    return d

def traverse(x, d, visited, counts, lim):
    visited, counts = visited.copy(), counts.copy()
    if x == 'end':
        return 1
    else:
        if x == x.lower():
            counts[x] += 1
            if any(i >= lim for i in counts.values()):
                visited |= set(list(counts.keys()))
        nxt = d[x] - visited
        if not nxt:
            return 0
        else:
            return sum(traverse(i, d, visited, counts, lim) for i in nxt)

if __name__ == '__main__':
    with open('src/day12/input.txt') as f:
        d = input2dict(f.read().strip())

    print("Part1:", traverse('start', d, set(['start']), defaultdict(int), 1))
    print("Part2:", traverse('start', d, set(['start']), defaultdict(int), 2))
