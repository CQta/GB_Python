kol = int(input())
col = 0
for i in range(kol):
    n = int(input())
    col += n
if col <= kol/2:
    print(col)
else:
    print(kol-col)


