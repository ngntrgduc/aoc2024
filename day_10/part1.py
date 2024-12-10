with open('input.txt', 'r') as f:
    data = f.read()

data = [[int(n) for n in line] for line in data.splitlines()]
h, w = len(data), len(data[0])

def in_map(x, y) -> bool:
    return (0 <= x < w) and (0 <= y < h)

def count_scores(x, y) -> int:
    count = 0
    current = data[x][y]
    if current == 9:
        if not mask[x][y]:
            mask[x][y] = 1
            return 1
        else:
            return 0

    # up
    if in_map(x, y - 1) and data[x][y - 1] == current + 1:
        count += count_scores(x, y - 1)
    # down
    if in_map(x, y + 1) and data[x][y + 1] == current + 1:
        count += count_scores(x, y + 1)
    # left
    if in_map(x - 1, y) and data[x - 1][y] == current + 1:
        count += count_scores(x - 1, y)
    # right
    if in_map(x + 1, y) and data[x + 1][y] == current + 1:
        count += count_scores(x + 1, y)

    return count

scores = 0
for i in range(h):
    for j in range(w):
        if data[i][j] == 0:
            mask = [[0] * w for _ in range(h)]
            scores += count_scores(i, j)

print(scores)