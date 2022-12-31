n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
rost = int(input())
mesto = 1
for i in lst:
    if i > rost:
        mesto += 1
print(mesto)
