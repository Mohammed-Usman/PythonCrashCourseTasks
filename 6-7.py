person_0={'first_name':'Muhammad','last_name':'Usman','Age':22,'City':'Karachi'}
#print(person_0['first_name'],person_0['last_name'],person_0['Age'],person_0['City'])

person_1 ={'first_name':'Shahid','last_name':'Afridi','Age':37,'City':'Khyber Agency'}
#print(person_1['first_name'],person_1['last_name'],person_1['Age'],person_1['City'])
people=[person_0,person_1]

for i in people[:]:
    for k,v in i.items():
        print(k,':',v)
    print('\n')