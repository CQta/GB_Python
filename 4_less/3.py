lst = list(input("Введите числа через пробел:\n").split())
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(new_lst)
