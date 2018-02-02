current_users = ['Ali','Taha','Tariq','Adnan','Usman','Admin','Hassan']
new_users = ['hammad','sohaib','tariq','ali','Umer','Hamza']
for i in range(0,len(current_users)):
    current_users[i] = current_users[i].upper()
print(current_users)
for new_user in new_users:
    if new_user.upper() in current_users:
        print('the person will need to enter a new username')
    else:
        print('the user name is available')