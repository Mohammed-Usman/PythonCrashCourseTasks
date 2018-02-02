counter=0
while True:
    counter += 1
    print('counter is =',counter)
    if int(counter) == 5:
        break
    age = input("Enter the person's age:")
    if int(age) < 3:
        print('the age is ' + age)
        print('movie ticket is free')
    elif int(age) >= 3 and int(age) <= 12:
        print('/n the age is ' + age)
        print('movie ticket cost $10')
    elif int(age) > 12:
        print('/n the age is ' + age)
        print('movie ticket cost $15')
        continue
