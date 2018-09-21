a = 1
b = 2
c = '3'
sum = 0
for x in (a,b,c):
    if isinstance(x, int):
        sum += x
print(sum)