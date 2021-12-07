def calibrate(x):
    return min(sum(abs(j - i) for j in x) for i in range(min(x), max(x)))

def triangulate(x):
    return min(sum(tri_n(abs(j - i)) for j in x) for i in range(min(x), max(x)))

def tri_n(n):
    return (n**2 + n) // 2

if __name__ == "__main__":
    with open("src/day07/input.txt") as f:
        x = [int(i) for i in f.read().strip().split(',')]

    print("Part1:", calibrate(x))
    print("Part2:", triangulate(x))
