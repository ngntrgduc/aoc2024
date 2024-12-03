with open('input.txt', 'r') as f:
    data = f.read()

def parse(instruct):
    return [int(number) for number in instruct[4:len(instruct)-1].split(',')]

import re
regex = r'mul\(\d{1,3},\d{1,3}\)'
result = 0
for instruct in re.findall(regex, data):
    a, b = parse(instruct)
    result += a * b 

print(result)
