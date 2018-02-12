file_name='pi_digits.txt'
i=0
with open(file_name) as file_object:
    for contents in file_object:
        i+=1
        print('line no_:',i,'=>',contents.lstrip())
        print()
    print('No_ of lines',i)
