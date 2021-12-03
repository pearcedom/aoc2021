from operator import ge, lt

def which_bit(x, compare):
    return '1' if compare(x.count('1'), len(x)/2) else '0'

def gamma_rate(x):
    return "".join(which_bit(i, ge) for i in zip(*x))

def epsilon_rate(x):
    return "".join(which_bit(i, lt) for i in zip(*x))

def get_rating(y, compare):
    i = 0
    while len(y) > 1:
        p = [j[i] for j in y]
        y = [j for j in y if j[i] == which_bit(p, compare)]
        i += 1
    return y[0]

def o2_rating(x):
    return get_rating(x, ge)

def co2_rating(x):
    return get_rating(x, lt)

if __name__ == "__main__":
    with open("src/day03/input.txt") as f:
        x = f.read().strip().split()

    print("Part1:", int(gamma_rate(x), 2) * int(epsilon_rate(x), 2))
    print("Part2:", int(o2_rating(x), 2) * int(co2_rating(x), 2))




