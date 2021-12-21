from functools import cache
from itertools import product

def play1(p1, p2, s1 = 0, s2 = 0, n = 1):
    if s1 >= 1000 or s2 >= 1000:
        return (n-1) * min(s1, s2)
    else:
        p1 = (p1 + sum(range(n, n+3))) % 10 or 10
        return play1(p2, p1, s2, s1 + p1, n+3)

@cache
def play2(p1, p2, s1 = 0, s2 = 0):
    if s1 >= 21 or s2 >= 21:
        return 1, 0
    else:
        w1, w2 = 0, 0
        for roll in (sum(i) for i in product([1,2,3], repeat=3)):
            nxt = (p1 + roll) % 10 or 10
            w2, w1 = [i+j for i, j in zip((w2, w1), play2(p2, nxt, s2, s1 + nxt))]
        return w1, w2

if __name__ == '__main__':
    print("Part1:", play1(7, 9))
    print("Part2:", max(play2(7, 9)))
