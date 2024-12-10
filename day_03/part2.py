with open('input.txt', 'r') as f:
    data = f.read()

def parse(instruct) -> list[int]:
    if not instruct:
        return 0, 0
    return [int(number) for number in instruct[4:len(instruct)-1].split(',')]

import re
regex = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
instructs = re.findall(regex, data)
l = len(instructs)
result = 0
i = 0

while i < l:
    instruct = instructs[i]
    if instruct == "don't()":
        while instruct != "do()":
            i += 1
            if i >= l:
                instruct = None
                break
            instruct = instructs[i]

    if instruct == "do()":
        i += 1
        continue

    a, b = parse(instruct)
    result += a * b 
    i += 1

print(result)
