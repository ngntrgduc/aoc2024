with open('input.txt', 'r') as f:
    data = f.read()

def remove_leading_zeros(stone):
    for i in range(len(stone)):
        if stone[i] != '0':
            return stone[i:]

    return '0'

def blink(stones):
    result = []
    for stone in stones:
        if stone == '0':
            result.append('1')
            continue
        
        stone_length = len(stone)
        if stone_length % 2 == 0:
            result.append(stone[:stone_length//2])
            result.append(remove_leading_zeros(stone[stone_length//2:]))
            continue

        result.append(str(int(stone) * 2024))

    return result

stones = data.split(' ')
for i in range(25):
    stones = blink(stones)

print(len(stones))