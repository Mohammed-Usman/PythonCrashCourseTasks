file_name='guest_book.txt'
with open(file_name,'a') as file_object:
    a=''
    while a!='quit':
        a = input('Enter Guest Name: ')
        if a!='quit':
            file_object.write(a+'\n')

with open(file_name) as file_object1:
    for contents in file_object1:
        print('Guests are',contents.rstrip())
