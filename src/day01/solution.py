def part1(x):
    return sum(j > i for i, j in zip(x[:-1], x[1:]))

def part2(x):
    return sum(j > i for i, j in zip(x[:-1], x[3:]))

if __name__ == "__main__":
    with open("src/day01/input.txt") as f:
        x = [int(i) for i in f.read().strip().split("\n")]

    print("Part1:", part1(x))
    print("Part2:", part2(x))
