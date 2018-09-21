age =input('Enter the age')
Age=int(age)
if Age<2:
    print('Person is a baby')
elif Age>=2 and Age<4:
    print('person is a toddler')
elif Age>=4 and Age<13:
    print('person is a kid')
elif Age>=13 and Age<20:
    print('person is a teenager')
elif Age>=20 and Age<64:
    print('person is adult')
elif Age==65:
    print('Person is adult')

