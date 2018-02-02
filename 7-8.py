sandwich_orders=['a','b','c','d','e','f','pastrami']
finished_sandwiches=[]
while sandwich_orders:
    a=sandwich_orders.pop()
    finished_sandwiches.append(a)
    print('ive made your',a,'sandwitch')
print(finished_sandwiches)
print(sandwich_orders)
