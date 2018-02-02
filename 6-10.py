num={'Usman'    :[2,32],
     'Zahid'    :[5,2,9],
     'Ali'      :[3,7,8],
     'Hassan'   :[9,1,4,3]}
for k,v in num.items():
    print(k+' favorite numbers are :')
    for a in v:
        print(a)
    print('.....')