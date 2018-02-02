usernames = ['Ali','Taha','Tariq','Adnan','Usman','Admin','Hassan']
for username in usernames:
    if username == 'Admin':
        print('\nHello admin,would you like to see a status report?\n')
    else:
        print('Hello '+username+ ', thank you for logging in again.')