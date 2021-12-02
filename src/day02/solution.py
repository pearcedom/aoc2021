import re

def part1(x):
    horizontal = depth = 0
    for cmd, n in x:
        match cmd:
            case 'forward':
                horizontal += n
            case 'down':
                depth += n
            case 'up':
                depth -= n
    return horizontal * depth

def part2(x):
    horizontal = depth = aim = 0
    for cmd, n in x:
        match cmd:
            case 'forward':
                horizontal += n
                depth += n * aim
            case 'down':
                aim += n
            case 'up':
                aim -= n
    return horizontal * depth

if __name__ == "__main__":
    with open("src/day02/input.txt") as f:
        x = []
        for i in f.read().strip().split('\n'):
            x.append([int(i) if i.isdigit() else i for i in re.split("\s+", i)])
        print("Part1:", part1(x))
        print("Part2:", part2(x))

