with open('input.txt', 'r') as f:
    data = f.read()

def check_block(block) -> bool:
    lr_diag = ''.join([block[i][i] for i in range(len(block))])
    if lr_diag != 'MAS' and lr_diag != 'SAM':
        return False
    
    block = block[::-1]  # reverse block
    rl_diag = ''.join([block[i][i] for i in range(len(block))])
    if rl_diag != 'MAS' and rl_diag != 'SAM':
        return False
    
    return True

data = data.splitlines()
l = len(data)
count = 0
for i in range(l - 3 + 1):
    for j in range(l - 3 + 1):
        block = [data[i+k][j:j+3] for k in range(3)]
        if check_block(block):
            count += 1


print(count)