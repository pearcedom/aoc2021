from math import prod
from operator import *

d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def reduce(out, value, t):
    fs = {0: sum, 1: prod, 2: min, 3: max,
        5: lambda x: gt(*x), 6: lambda x: lt(*x), 7: lambda x: eq(*x)}
    return fs[t](out), value

def parse(packet):
    v, t, value = packet[0:3], int(packet[3:6], 2), packet[6:]
    return parse_literal(value) if t == 4 else reduce(*parse_operator(value), t)

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
