cities={'Karachi':
                {'country':'Pakistan',
                 'population':'21.2 million',
                 'fact':'Karachi is more than 4 times the size of New York City.'},
        'Ankara':
                {'country':'Turkey',
                'population':'5.271 million',
                'fact':'Ankara is the place to eat an authentic kebab,'
                       'from a huge rotating meat skewer.'},
        'Baghdad':
                {'country':'Iraq',
                'population':'7.665 million',
                'fact':'It was almost destroyed by the Mongols in 1258.'}}
for k,v in cities.items():
    print('|'+k.title()+':')
    for key,values in v.items():
        print('|'+key.title()+' => '+values)
    print('---------------------------------------------------------------------')


