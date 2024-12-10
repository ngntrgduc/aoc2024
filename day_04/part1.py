with open('input.txt', 'r') as f:
    data = f.read()

def count_xmas(line: str) -> int:
    return line.count('XMAS') + line.count('SAMX')

def check_diag(data) -> int:
    l = len(data)
    # main diag
    count = count_xmas(''.join([data[i][i] for i in range(l)]))

    # upper and lower diags
    for i in range(1, l-4):
        upper_diag = [data[row][i+row] for row in range(0, l-i)]
        lower_diag = [data[row+i][row] for row in range(0, l-i)]
        count += count_xmas(''.join(upper_diag)) + count_xmas(''.join(lower_diag))

    return count

data = data.splitlines()
count = 0

# check horizontal
for line in data:
    count += count_xmas(line)

# check vertical
for j in range(len(data[0])):
    column = ''.join([line[j] for line in data])
    count += count_xmas(column)

# check diagonal 
count += check_diag(data)  # from left to right
count += check_diag([line[::-1] for line in data])  # from right to left

print(count)