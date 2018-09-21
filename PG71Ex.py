food=('item1','item2','item3','item4','item5')
for i in food:
    print (i)


list1 = list(food)
list1[0]='aaaa'
list1[3]='bbbb'
food = tuple(list1)
print(food)
