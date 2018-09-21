import numpy as np

array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])
sum=array1+array2
#sum=sum(array1,array2)
print(sum)

array3 = np.linspace(0,10,15)
print(array3)

m=np.arange(1,10).reshape(3,3)
print(m)
size=np.size(m,0)
print(size)

print(m[:,1])
print()
print(m[:2,:-1])


pipe=((array1<2))|(array2>3)
print(pipe)

n=np.arange(1,10).reshape(3,3)
print('n=:\n',n)
print('Transpose of n \n',n.transpose())
