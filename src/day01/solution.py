def adjacent_increases(x, offset = 1):
    return sum(j > i for i, j in zip(x[:-1], x[offset:]))

if __name__ == "__main__":
    with open("src/day01/input.txt") as f:
        x = [int(i) for i in f.read().strip().split("\n")]

    print("Part1:", adjacent_increases(x))
    print("Part2:", adjacent_increases(x, 3))
