sandwich_orders=['a','pastrami','b','c','pastrami','d','e','f','pastrami']
finished_sandwiches=[]
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    a=sandwich_orders.pop()
    finished_sandwiches.append(a)
    print('ive made your',a,'sandwitch')
print(finished_sandwiches)
print(sandwich_orders)