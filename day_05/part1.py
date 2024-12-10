with open('input.txt', 'r') as f:
    data = f.read()

rules, updates = data.split('\n\n')
rules = [rule.split('|') for rule in rules.splitlines()]
rules = [(int(before), int(after)) for before, after in rules]
updates = updates.splitlines()
middle_sum = 0

for update in updates: 
    is_right_order = True
    update = [int(number) for number in update.split(',')]
    for rule in rules:
        before, after = rule
        if before not in update or after not in update:
            continue
        
        if update.index(before) > update.index(after):
            is_right_order = False
            break
        
    if is_right_order:
        middle_sum += update[len(update) // 2]

print(middle_sum)