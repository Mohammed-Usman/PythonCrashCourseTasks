toppings=[]
a=''
while a!='quit':
    a=input('Enter the toppings you want to add')
    if a!='quit':
        toppings.append(a)
        print('You enter these toppngs',toppings)
print('You added these toppings')
for i in toppings[:]:
    print(i)