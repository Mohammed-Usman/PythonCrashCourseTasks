'''
a=['xaa','xzz','axx','bbb','ccc']
b=[]
c=[]
for i in range(len(a)):
    b=a[i]
    if b[0]=='x':
     c.append(b)
print(c)

a=['xaa','xzz','axx','bbb','ccc']
c=[]
b=[]
for i in range(len(a)):
    c=a[i]
    b.append(c)
    print(b)
print()
print(b)
===========================================
squares=[value for value in range(1,11)]
print(squares)
print('//////////////////////////////////////////////////')
squares=[]
for value in range(1,11):
    squares.append(value)

print(squares)
'''
a=['xaa','xzz','axx','bbb','ccc']
b=[]
c=[]
b=[(i/i) for i in range(len(a)+1)]
#for i in range(len(a)/j):
print(a.pop(b))
#print(b)
#c=a.pop(b)
print(b)
print()
print(c)