from functools import lru_cache

@lru_cache(maxsize=None)
def n_after(x, n):
    if n == 0:
        return 1
    else:
        if x > 0:
            return n_after(x-1, n-1)
        else:
            return n_after(6, n-1) + n_after(8, n-1)

if __name__ == "__main__":
    with open("src/day06/input.txt") as f:
        x = [int(i) for i in f.read().strip().split(',')]
    print("Part1:", sum(n_after(i, 80) for i in x))
    print("Part2:", sum(n_after(i, 256) for i in x))
