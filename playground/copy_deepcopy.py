from copy import copy, deepcopy

def display(a, b) -> None:
    print(f'{a = }'), print(f'{b = }')

print(' - "=" operator: b = a')
a = [1, 2, 3, 4, [5, 6]]
b = a
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}')
a.append(0), print('-> a.append(0)')
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}\n')


print(' - Shallow copy: b = copy(a)')
a = [1, 2, 3, 4, [5, 6]]
b = copy(a)
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}')
a.append(0), print('-> a.append(0)')
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}')
a[4].append(7), print('-> a[4].append(7)')
display(a, b)
print(f'b[4] is a[4]: {b[4] is a[4]}\nb[4] == a[4]: {b[4] == a[4]}\n')


print(' - Deep copy: b = deepcopy(a)')
a = [1, 2, 3, 4, [5, 6]]
b = deepcopy(a)
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}')
a.append(0), print('-> a.append(0)')
display(a, b)
print(f'b is a: {b is a}\nb == a: {b == a}')
a[4].append(7), print('-> a[4].append(7)')
display(a, b)
print(f'b[4] is a[4]: {b[4] is a[4]}\nb[4] == a[4]: {b[4] == a[4]}')