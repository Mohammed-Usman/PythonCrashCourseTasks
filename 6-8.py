tom     ={'owner':'Tedd','kind':'cat'}
mickey   ={'owner':'Sarah','kind':'parrot'}
jerry   ={'owner':'Jef','kind':'mouse'}
pet_list=[tom,mickey,jerry]

for pet in pet_list[0:len(pet_list)]:
    for k,v in pet.items():
        print(k,':',v)
    print()
#dictionary ka name nai print ho rha