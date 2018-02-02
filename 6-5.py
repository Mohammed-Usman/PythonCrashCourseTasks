rivers={'nile'          :   'egypt',
        'indus'         :'Pakistan',
        'Ganga Jumna'   :'India'}
for k,v in rivers.items():
    print('The ',k.title(),' runs through ',v)
print('\nName of Rivers')
for k in rivers.keys():
    print(k.title())
print('\nName of Countries')
for k in rivers.values():
    print(k.title())