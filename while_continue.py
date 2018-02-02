active = True
counter=0
while active:
    message = input('prompt')
    if message == 'quit':
        active = False
    else:
        counter += 1
        if counter==5:
            active= False
        print(message)