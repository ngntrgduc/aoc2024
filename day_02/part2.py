with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

def check_tolerate(levels) -> bool:
    count_unsafe = 0
    for i in range(len(levels) - 1):
        if levels[0] <= levels[1]:
            if levels[i+1] - levels[i] not in [1, 2, 3]:
                count_unsafe += 1
        else:
            if levels[i] - levels[i+1] not in [1, 2, 3]:
                count_unsafe += 1

    if count_unsafe <= 1:
        return True

    return False

count_tolerate = 0
for line in data:
    levels = [int(number) for number in line.split(' ')]
    if check_tolerate(levels):
        count_tolerate += 1

print(count_tolerate)
