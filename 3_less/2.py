lst = list(map(int, input().split()))
l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
for i in range(l):
    print(lst[i]*lst[0-i-1])
