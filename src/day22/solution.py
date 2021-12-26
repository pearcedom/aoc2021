import re
from collections import defaultdict

def volume(x, y, z):
    ax = x[1] - x[0] + 1
    ay = y[1] - y[0] + 1
    az = z[1] - z[0] + 1
    return ax*ay*az

def intersect_range(x, y, z, x_, y_, z_):
    xi = max(x[0], x_[0]), min(x[1], x_[1])
    yi = max(y[0], y_[0]), min(y[1], y_[1])
    zi = max(z[0], z_[0]), min(z[1], z_[1])
    return xi, yi, zi

def reboot(steps):
    ons, offs = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for step in steps:
        state, dims = step.split(" ")
        x, y, z = [(int(i), int(j)) for i, j in re.findall("(-{0,1}\d+)..(-{0,1}\d+)", dims)]
        on_keys, off_keys = ons.copy().keys(), offs.copy().keys()
        # Penalise intersection between current & previous 'ons'
        for x_, y_, z_ in on_keys:
            xi, yi, zi = intersect_range(x, y, z, x_, y_, z_)
            if xi[0] <= xi[1] and yi[0] <= yi[1] and zi[0] <= zi[1]:
                offs[xi, yi, zi] += volume(xi, yi, zi)
        # 'Penalise' intersection between current & previous 'offs'
        for x_, y_, z_ in off_keys:
            xi, yi, zi = intersect_range(x, y, z, x_, y_, z_)
            if xi[0] <= xi[1] and yi[0] <= yi[1] and zi[0] <= zi[1]:
                ons[xi, yi, zi] += volume(xi, yi, zi)
        # Add if on regardless
        if state == 'on':
            ons[x, y, z] += volume(x, y, z)
    return sum(ons.values()) - sum(offs.values())

if __name__ == '__main__':
    with open('src/day22/input.txt') as f:
        steps = f.read().splitlines()
        print("Part1:", reboot(steps[:20]))
        print("Part2:", reboot(steps))

#      ------
#   ------
# | | | | | | | | |
# 1 2 3 4 5 6 7 8 9
#
#          ------
#   ------
# | | | | | | | | |
# 1 2 3 4 5 6 7 8 9
#
#            ------
#   ------
# | | | | | | | | |
# 1 2 3 4 5 6 7 8 9
#
# ..... | .....
# .###. | .+++.
# .###. | .+++.
# .###. | .+++.
# ..... | .....
# ..... | .....
#       |
# ..... | ..... ..... .....
# ..... | .+++. ..... .....
# ..### | .+++. ..+++ ..--.
# ..### | .+++. ..+++ ..--.
# ..### | ..... ..+++ .....
# ..... | ..... ..... .....
#       |
# MMM.. | ..... ..... ..... | ..... ..... .....
# MMM.. | .+++. ..... ..... | .--.. ..... .....
# MMM.. | .+++. ..+++ ..--. | .--.. ..-.. ..+..
# ..... | .+++. ..+++ ..--. | ..... ..... .....
# ..... | ..... ..+++ ..... | ..... ..... .....
# ..... | ..... ..... ..... | ..... ..... .....
#       |
# ..... | ..... ..... ..... | ..... ..... ..... | ..... ..... .....
# .#... | .+++. ..... ..... | .--.. ..... ..... | .+... .-... .+...
# ..... | .+++. ..+++ ..--. | .--.. ..-.. ..+.. | ..... ..... .....
# ..... | .+++. ..+++ ..--. | ..... ..... ..... | ..... ..... .....
# ..... | ..... ..+++ ..... | ..... ..... ..... | ..... ..... .....
# ..... | ..... ..... ..... | ..... ..... ..... | ..... ..... .....
#
# ..... | ..... ..... ..... | ..... ..... ..... | ..... ..... .....
# .M... | .+++. ..... ..... | .--.. ..... ..... | .+... .-... .+...
# ..... | .+++. ..+++ ..--. | .--.. ..-.. ..+.. | ..... ..... .....
# ..... | .+++. ..+++ ..--. | ..... ..... ..... | ..... ..... .....
# ..... | ..... ..+++ ..... | ..... ..... ..... | ..... ..... .....
# ..... | ..... ..... ..... | ..... ..... ..... | ..... ..... .....
