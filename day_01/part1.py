with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

left, right = [], []
for line in data:
    if not line:
        continue
    line_split = line.split('   ')
    left.append(int(line_split[0]))
    right.append(int(line_split[1]))

distance = 0
left_sorted = sorted(left)
right_sorted = sorted(right)
for l, r in zip(left_sorted, right_sorted):
    distance += abs(l - r)

print(distance)
