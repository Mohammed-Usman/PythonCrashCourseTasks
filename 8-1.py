def update_list(sandwich_orders):
    finished_sandwiches=[]
    while sandwich_orders:
        a=sandwich_orders.pop()
        finished_sandwiches.append(a)
        print('ive made your',a,'sandwitch')
    print('finished_sandwihtches',finished_sandwiches)
    print(sandwich_orders)
update_list(['a','b','c','d','e','f','pastrami'])
update_list([1,2,3,4,5,6,7])
update_list(['abcd','Abcd','3434','dghd','eeeee','fffff','pastrami'])
