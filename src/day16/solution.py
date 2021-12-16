from math import prod

d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def parse(packet):
    v, t, value = packet[0:3], int(packet[3:6], 2), packet[6:]
    if t == 4:
        return parse_literal(value)
    else:
        out, value = parse_operator(value)
        if t == 0:
            out = sum(out)
        elif t == 1:
            out = prod(out)
        elif t == 2:
            out = min(out)
        elif t == 3:
            out = max(out)
        elif t == 5:
            out = int(out[0] > out[1])
        elif t == 6:
            out = int(out[0] < out[1])
        elif t == 7:
            out = int(out[0] == out[1])
        return out, value

def parse_operator(value):
    lt_id, value = value[0], value[1:]
    if lt_id == '0':
        l, value = value[0:15], value[15:]
        ns = []
        l_start = len(value)
        while l_start - len(value) < int(l, 2):
            n, value = parse(value)
            ns += [n]
    elif lt_id == '1':
        l, value = value[0:11], value[11:]
        l = int(l, 2)
        ns = []
        while l > 0:
            n, value = parse(value)
            ns += [n]
            l -= 1
    return ns, value

def parse_literal(value):
    lit = ""
    while True:
        i, group, value = value[0], value[1:5], value[5:]
        lit += group
        if i == '0':
            break
    return int(lit, 2), value

if __name__ == '__main__':
    with open('src/day16/input.txt') as f:
        packet = "".join([d[i] for i in f.read().strip()])

    print("Part1: I just shonked this by printing to stdout,",
        "\n  copy pasting and post-processing... not reproducible!")
    print("Part2:", parse(packet)[0])
