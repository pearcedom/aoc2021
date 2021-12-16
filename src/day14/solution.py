from collections import Counter
from functools import lru_cache, reduce
from operator import add

def insert(x, rules, n):
    @lru_cache(maxsize=None)
    def f(x, n):
        (first, last), mid = x, rules[x]
        if n <= 0:
            return Counter(last)
        else:
            return f(first+mid, n-1) + f(mid+last, n-1)
    return Counter(x[0]) + f(x, n)

def solve(x, rules, n):
    count = reduce(add, [insert(i, rules, n) for i in x])
    return max(count.values()) - min(count.values())

if __name__ == '__main__':
    with open('src/day14/input.txt') as f:
        polymer, rules = f.read().strip().split("\n\n")
        polymer = [polymer[i:i+2] for i in range(len(polymer)-1)]
        rules = dict(tuple(i.split(" -> ")) for i in rules.split('\n'))
    print("Part1:", solve(polymer, rules, 10))
    print("Part2:", solve(polymer, rules, 40))
