with open('input.txt', 'r') as f:
    data = f.read()

data = data.splitlines()
h, w = len(data), len(data[0])
visited = [[0]*w for _ in range(h)]
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
        direction = change_direction(direction)
        row, col = position  # Not update position

    return (row, col), direction
    
# get character position
direction = '^'
for row in range(h):
    if direction not in data[row]:
        continue
    col = data[row].index(direction)
    position = (row, col)

while not can_leave(position, direction):
    row, col = position
    if visited[row][col] == 0:
        visited[row][col] = 1
        count += 1

    position, direction = go(position, direction)

print(count + 1)  # 4988