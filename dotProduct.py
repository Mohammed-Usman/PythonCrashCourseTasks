import numpy as np

a=[0,1,2,3]
b=[0,1,2,3]
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print(sum(c))

a=[x*y for x,y in zip(a,b)]
print(sum(a))
print('------------------------------------------------------------------------------------------------')
m = np.array([np.arange(5),np.arange(5),np.arange(5)])
print(m)
print(m.shape)
print(m[1,2])
print('------------------------------------------------------------------------------------------------')
