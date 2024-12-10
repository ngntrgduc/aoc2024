data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


data = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""

with open('input.txt', 'r') as f:
    data = f.read()

data = [[c for c in line] for line in data.splitlines()]
h, w = len(data), len(data[0])

def display(data):
    print('\n'.join([''.join(line) for line in data]))

def in_map(x, y):
    """Check if the position is in map"""
    return (0 <= x < w) and (0 <= y < h)

from copy import deepcopy
def count_anitodes(a, b):
    """Count anitodes with direction from a -> b"""
    # print(f'{a = }, {b = }')
    count = 0
    x_a, y_a = a
    x_b, y_b = b
    x, y = x_a, y_a  # in case if x_a = x_b and y_a = y_b
    dx = abs(x_b - x_a)
    dy = abs(y_b - y_a)

    if x_a < x_b:
        x = x_b + dx
        if y_a < y_b:   y = y_b + dy
        elif y_a > y_b: y = y_b - dy
    elif x_a > x_b:
        x = x_b - dx
        if y_a < y_b:   y = y_b + dy
        elif y_a > y_b: y = y_b - dy

    # print(f'{x = }, {y = }')
    if not in_map(x, y):
        return 0

    if data[x][y] == '.':
        data[x][y] = '#'  # add anitode to the map
        # display(data)
        # print('+1')
        # return 1 + count_anitodes(b, (x, y))
        count +=  1 + count_anitodes(b, (x, y))
    else:
        # display(data)
        if data[x][y] != '#':  # the position is antenna
            # print('+1')
            # return 1 + count_anitodes(b, (x, y))
            count +=  count_anitodes(b, (x, y))

    # print('')
    # return 0
    return count

    if data[x][y] == '.':
        data[x][y] = '#'  # add anitode to the map
        return 1
    else:
        if data[x][y] != '#':  # the position is antenna
            return 1 
    return 0


def check(positions):
    count = 0
    for position in positions.values():
        for i in range(len(position) - 1):
            for j in range(i+1, len(position)):
                count += count_anitodes(position[i], position[j])  # a -> b
                count += count_anitodes(position[j], position[i])  # b -> a

    return count

positions = {}  # store positions of frequencies
for i in range(h):
    for j in range(w):
        character = data[i][j]
        if character == '.':
            continue

        if character not in positions:
            positions.update({character: []})

        positions[character].append((i, j))

print(positions)
print(check(positions) + sum([len(position) for position in positions.values()]))
# display(data)
# for i in range(h):
#     for j in range(w):
#         character = data[i][j]
#         if character == '#':
#             continue

# 27 new antinodes appears on the map
# so how it = 34 wtf

# false: 995