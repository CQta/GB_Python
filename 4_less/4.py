import random

k = int(input("Введите натуральную степень k = "))
kf = [random.randint(0, 101) for i in range(k+1)]
lst = kf[::-1]
x = ''
if len(lst) < 1:
    wr = 'x = 0'
else:
    for i in range(len(lst)):
        if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
            x += f'{lst[i]}x^{len(lst)-i-1}'
            if lst[i+1] != 0:
                x += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            x += f'{lst[i]}x'
            if lst[i+1] != 0:
                x += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            x += f'{lst[i]} = 0'
        elif i == len(lst) - 1 and lst[i] == 0:
            x += ' = 0'
with open('file33.txt', 'w') as data:
    data.write(x)