# Due to my skill issue, I did not finish this part
# Refernce: https://www.youtube.com/watch?v=NYi74ooakgA
# Idea: Using Topological Sort

with open('input.txt', 'r') as f:
    data = f.read()

def is_correct_order(update, rules):
    is_right_order = True        
    for rule in rules:
        before, after = rule

        if update.index(before) > update.index(after):
            is_right_order = False
            break

    return is_right_order

def fix_order(update, rule_contained):
    for rule in rule_contained:                
        original = update
        before, after = rule
        if not is_correct_order(update, rule_contained):
            print(f' -> violate rule {rule}')
            update.remove(before)
            update.insert(update.index(after), before)
            
            update.remove(after)
            update.insert(update.index(before)+1, after)

    return update

rules, updates = data.split('\n\n')
rules = [rule.split('|') for rule in rules.splitlines()]
rules = [(int(before), int(after)) for before, after in rules]
updates = updates.splitlines()
middle_sum = 0

for update in updates: 
    is_right_order = True
    update = [int(number) for number in update.split(',')]
    
    rule_contained = []
    for rule in rules:
        before, after = rule
        if before not in update or after not in update:
            continue
        
        if before in update and after in update:
            rule_contained.append((before, after))

        if update.index(before) > update.index(after):
            is_right_order = False
            break

    if not is_right_order:
        print(f'update: {update}')
        print(f' - rule contained: {rule_contained}')
        fixed = fix_order(update, rule_contained)
        print(f' - after fixed: {fixed}')
        print()
        middle_sum += fixed[len(fixed) // 2]

print(middle_sum)
# false: 5865 low, 5888 low, 6504, 6528, 6366 high, 6104, 6403, 6411