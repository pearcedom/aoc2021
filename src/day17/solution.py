if __name__ == '__main__':
    tx, ty = range(124, 175), range(-123, -85)

    max_ys = []
    successes = set()
    for x in range(0, max(tx)+1):
        for y in range(min(ty), abs(min(ty))):
            c = 0, 0
            v = w = x, y
            max_y = 0
            while c[0] < max(tx) and c[1] > min(ty):
                c = tuple(i + j for i, j in zip(c, v))
                max_y = max(max_y, c[1])
                v = v[0]-1 if v[0] > 0 else 0, v[1]-1
                if c[0] in tx and c[1] in ty:
                    max_ys.append(max_y)
                    successes |= set([w])

    print("Part1:", max(max_ys))
    print("Part2:", len(successes))
