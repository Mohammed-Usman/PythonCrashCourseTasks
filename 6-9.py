favorite_places={'Ali'      :['Lahore','Multan'],
                 'Hassan'   :['Karachi','Sibbi','Muree'],
                 'Umer'     :['Pindi','Islamabad','Quetta']
                 }
for k,v in favorite_places.items():
    print('Favorite places of '+k+':')
    for places in v:
        print(places)
    print()