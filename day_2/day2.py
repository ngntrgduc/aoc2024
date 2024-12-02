with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')


# Part 1
def check(levels) -> bool:
    if levels[0] == levels[1]:
        return False

    for i in range(len(levels) - 1):
        if levels[0] < levels[1]:
            if levels[i+1] - levels[i] not in [1, 2, 3]:
                return False
        else:
            if levels[i] - levels[i+1] not in [1, 2, 3]:
                return False

    return True


# Part 2
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


# Result
count = 0
count_tolerate = 0
for line in data:
    levels = [int(number) for number in line.split(' ')]
    if check(levels):
        count += 1
    if check_tolerate(levels):
        count_tolerate += 1
    
print(f'Part 1: {count}')
print(f'Part 2: {count_tolerate}')