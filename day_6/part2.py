with open('input.txt', 'r') as f:
    data = f.read()

data = data.splitlines()
data = [[char for char in line] for line in data]
h, w = len(data), len(data[0])
count = 0
directions = ['^', '>', 'v', '<']

def can_leave(position, direction) -> bool:
    row, col = position
    if (row == h - 1 and direction == 'v') \
    or (row == 0 and direction == '^') \
    or (col == 0 and direction == '<') \
    or (col == w - 1 and direction == '>'):
        return True

    return False

def is_obstacle(row, col) -> bool:
    return data[row][col] == '#'

def change_direction(direction) -> str:
    return directions[(directions.index(direction) + 1) % len(directions)]

def go(position, direction) -> tuple[int]:
    row, col = position
    if direction == '^': row -= 1
    if direction == '>': col += 1
    if direction == 'v': row += 1
    if direction == '<': col -= 1

    if is_obstacle(row, col):
        row, col = position  # Not update position
        direction = change_direction(direction)
    
    if can_leave((row, col), direction):
        return (row, col), direction

    return (row, col), direction

# get character position
direction = '^'
for row in range(h):
    if direction not in data[row]:
        continue
    col = data[row].index(direction)
    position = (row, col)

# get path visited, reduce cases to check
visited = [[0]*w for _ in range(h)]
temp_position, temp_direction = position, direction
while not can_leave(temp_position, temp_direction):
    row, col = temp_position
    if visited[row][col] == 0:
        visited[row][col] = 1
    
    temp_position, temp_direction = go(temp_position, temp_direction)

def is_loop(slow, slow_direction, fast, fast_direction) -> bool:
    """Check loop using Tortoise and Hare algorithm"""
    while not can_leave(fast, fast_direction):
        if fast == slow and fast_direction == slow_direction:
            return True

        slow, slow_direction = go(slow, slow_direction)
        fast, fast_direction = go(fast, fast_direction)
        if can_leave(fast, fast_direction):
            return False
        fast, fast_direction = go(fast, fast_direction)
    return False

import copy
original_data = data
for i in range(h):
    for j in range(w):
        if visited[i][j] == 0:
            continue

        data = copy.deepcopy(original_data)
        data[i][j] = '#'
        slow, slow_direction = position, direction
        fast, fast_direction = go(slow, slow_direction)
        if is_loop(slow, slow_direction, fast, fast_direction):
            count += 1

print(count + 1)  # 1697