import re

def pilot(x):
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
    return horizontal, depth, aim

if __name__ == "__main__":
    with open("src/day02/input.txt") as f:
        x = []
        for i in f.read().strip().split('\n'):
            x.append([int(i) if i.isdigit() else i for i in re.split("\s+", i)])
        h, d, a = pilot(x)
        print("Part1:", h * a)
        print("Part2:", h * d)
