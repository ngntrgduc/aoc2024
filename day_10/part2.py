with open('input.txt', 'r') as f:
    data = f.read()

data = [[int(n) for n in line] for line in data.splitlines()]
h, w = len(data), len(data[0])

def in_map(x, y) -> bool:
    return (0 <= x < w) and (0 <= y < h)

def count_ratings(x, y) -> int:
    count = 0
    current = data[x][y]
    if current == 9:
        return 1

    #               up      down     left    right  
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if in_map(new_x, new_y) and data[new_x][new_y] == current + 1:
            count += count_ratings(new_x, new_y)

    return count

ratings = 0
for i in range(h):
    for j in range(w):
        if data[i][j] == 0:
            mask = [[0] * w for _ in range(h)]
            ratings += count_ratings(i, j)

print(ratings)
