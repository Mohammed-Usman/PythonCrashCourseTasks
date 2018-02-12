from user_privileges_administrator import Administrator

admin = Administrator('Zahid', 'Naseem', 23, 'Male')
admin.privl.show_privileges()
print()
admin.describe_user()