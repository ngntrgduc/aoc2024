with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

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

# Result
count = 0
for line in data:
    levels = [int(number) for number in line.split(' ')]
    if check(levels):
        count += 1
    
print(count)
