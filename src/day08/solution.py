# rushed!

segment_map = {
    0: {'top', 'top_left', 'top_right', 'bottom_left', 'bottom_right', 'bottom'},
    1: {'top_right', 'bottom_right'},
    2: {'top', 'top_right', 'mid', 'bottom_left', 'bottom'},
    3: {'top', 'top_right', 'mid', 'bottom_right', 'bottom'},
    4: {'top_left', 'top_right', 'mid', 'bottom_right'},
    5: {'top', 'top_left', 'mid', 'bottom_right', 'bottom'},
    6: {'top', 'top_left', 'mid', 'bottom_left', 'bottom_right', 'bottom'},
    7: {'top', 'top_right', 'bottom_right'},
    8: {'top', 'top_left', 'top_right', 'mid', 'bottom_left', 'bottom_right', 'bottom'},
    9: {'top', 'top_left', 'top_right', 'mid', 'bottom_right', 'bottom'}
}

segment_counts = {
    4: 'bottom_left',
    6: 'top_left',
    7: 'mid',
    8: 'top_right',
    9: 'bottom_right'
}

def count_1478(xs):
    count = 0
    for x in xs:
        _1478 = get_1478(x[0])
        count += len([i for i in x[1] if set(i) in _1478])
    return count

def get_1478(patterns):
    patterns.sort(key = lambda x: len(x))
    return [set(patterns[i]) for i in [0, 2, 1, 9]]

def decrypt(patterns):
    cipher = {i: segment_counts[sum(j.count(i) for j in patterns)] for i in 'abcdefg'}
    one, four, seven, eight = get_1478(patterns)
    top = set(seven) - set(one)
    bottom_left = set(i for i, j in cipher.items() if j == "bottom_left")
    bottom = set('abcdefg') - set(four) - top - bottom_left
    cipher.update([
        (list(top)[0], 'top'),
        (list(bottom_left)[0], 'bottom_left'),
        (list(bottom)[0], 'bottom'),
    ])
    return cipher

def translate(patterns, signal):
    cipher = decrypt(patterns)
    out = ""
    for sig in signal:
        signal_set = set(cipher[i] for i in sig)
        for i, j in segment_map.items():
            if signal_set == j:
                out += str(i)
    return int(out)

if __name__ == "__main__":
    with open("src/day08/input.txt") as f:
        xs = []
        for l in f.read().splitlines():
            patterns, signal = [[j for j in i.split()] for i in l.split("|")]
            xs.append((patterns, signal))

    print("Part1:", count_1478(xs))
    print("Part2:", sum(translate(*x) for x in xs))

#  aaaa
# b    c
# b    c
#  dddd        _     _  _       _   _  _   _   _
# e    f      | | |  _| _| |_| |_  |_   | |_| |_|
# e    f      |_| | |_  _|   |  _| |_|  | |_|  _|
#  gggg



