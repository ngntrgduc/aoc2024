import copy

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def combination(result, numbers, combinated=0):
    count = 0
    if not numbers:
        return 1 if combinated == result else 0

    numbers = copy.deepcopy(numbers)
    current = numbers.pop(0)

    count += combination(result, numbers, combinated + current)
    if count:
        return count

    if combinated == 0:
        combinated = 1  # for multiplication

    count += combination(result, numbers, combinated * current)    
    return count

total = 0
for line in data:
    result, numbers = line.split(': ')
    result, numbers = int(result), [int(number) for number in numbers.split(' ')]
    if combination(result, numbers):
        total += result

print(total)