n = int(input())
s = float(0)
for i in range(n-1):
    s += (1/pow(16, i))*(4/((8*i)+1) - 2/((8*i)+4)-1/((8*i)+5)-1/((8*i)+6))
print(round(s, n))


