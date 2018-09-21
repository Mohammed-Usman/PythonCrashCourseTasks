import random
document=[1,2,3,4,5,6,7,8,9]

for i,document in enumerate(document):
    print(i,'=>',document)
print('---------------------------------------------------------------------------')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [1.5,2.3,5.8,1.0,5.0]
for el in zip(list1,list2,list3):
    print(el)

print('---------------------------------------------------------------------------')
a= random.sample(range(10),10)
b= random.sample(range(10),10)
c= random.sample(range(10),10)
print('random array1:\n',a)
print('random array2:\n',b)
print('random array3:\n',c)

sm=[sum(x) for x in zip(a,b,c)]

print('Sum of a,b,c',sm)

