with open('input.txt', 'r') as f:
    data = f.read()

data = [[c for c in line] for line in data.splitlines()]
h, w = len(data), len(data[0])

def in_map(x, y):
    """Check if the point is in map"""
    return (0 <= x < w) and (0 <= y < h)

def count_anitodes(a, b):
    """Count anitodes with direction from a -> b"""
    x_a, y_a = a
    x_b, y_b = b
    x, y = x_a, y_a  # in case if x_a = x_b and y_a = y_b
    dx = abs(x_b - x_a)
    dy = abs(y_b - y_a)

    if x_a < x_b:
        x = x_b + dx
        if y_a < y_b:   y = y_b - dy
        elif y_a > y_b: y = y_b + dy
    elif x_a > x_b:
        x = x_b - dx
        if y_a < y_b:   y = y_b + dy
        elif y_a > y_b: y = y_b - dy

    if in_map(x, y) and data[x][y] == '.':
        data[x][y] = '#'  # add anitode to the map
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

print(check(positions))