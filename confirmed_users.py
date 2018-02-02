unconfirmed_users=['alice','brian','candace']
confrimed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Varifying user: "+current_user.title())
    confrimed_users.append(current_user)
print('The following users have been confirmed: ')
for confrimed_user in confrimed_users:
        print(confrimed_user)
