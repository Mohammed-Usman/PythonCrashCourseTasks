alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[]

#Make 30 green aliens
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print('...')
print("The total number of aliens : "+str(len(aliens))+'\n')

#First 3 aliens
for aliena in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] == 10
for alien in aliens[:5]:
    print(alien)
print('...')