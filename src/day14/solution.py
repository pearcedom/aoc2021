from collections import Counter
from functools import lru_cache, reduce
from operator import add

def couplet(x):
    return x[0:2], x[1:3]

def kmers(x, k):
    return [x[i:i+k] for i in range(len(x)-1)]

def insert(x, rules, n):
    @lru_cache(maxsize=None)
    def f(x, n):
        if n <= 0:
            return Counter(x[1])
        else:
            return reduce(add, [f(i, n-1) for i in couplet(rules[x])])
    return Counter(x[0]) + f(x, n)

def solve(x, rules, n):
    count = reduce(add, [insert(i, rules, n) for i in kmers(x, 2)])
    return max(count.values()) - min(count.values())

if __name__ == '__main__':
    with open('src/day14/input.txt') as f:
        polymer, rules = f.read().strip().split("\n\n")
        rules = [tuple(i.split(" -> ")) for i in rules.split('\n')]
        rules = dict((i, "".join([i[0], j, i[1]])) for i, j in rules)
    print("Part1:", solve(polymer, rules, 10))
    print("Part2:", solve(polymer, rules, 40))
