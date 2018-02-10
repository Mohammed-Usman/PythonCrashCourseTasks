class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=0


    def reset_login_attempts(self):
        '''Login Attempts resets to 0'''
        self.login_attempts = 0
        print(self.login_attempts)

    def increment_login_attempts(self):

        self.login_attempts+=1
        return self.login_attempts

    def describe_user(self):

        print('First Name: ',self.first_name)
        print('Lasr Name: ',self.last_name)
        print('Age is: ',self.age)
        print('Gender is: ',self.gender)

    def greet_user(self):

        print('Hello',self.first_name,'\n')


first_person=User('Muhammad','Usman',22,'M')
second_person=User('Hassan','ALi',18,'M')
third_person=User('Zohaib','Farooqi',23,'M')


first_person.describe_user()
print('Login Attempts',first_person.increment_login_attempts())
#first_person.reset_login_attempts()    '''Login Attempts resets to 0'''
first_person.greet_user()

first_person.describe_user()
print('Login Attempts',first_person.increment_login_attempts())
#first_person.reset_login_attempts()    '''Login Attempts resets to 0'''
first_person.greet_user()


second_person.describe_user()
print('Login Attempts',second_person.increment_login_attempts())
second_person.greet_user()

second_person.describe_user()
print('Login Attempts',second_person.increment_login_attempts())
second_person.greet_user()

third_person.describe_user()
print('Login Attempts',third_person.increment_login_attempts())
third_person.greet_user()

third_person.describe_user()
print('Login Attempts',third_person.increment_login_attempts())
third_person.greet_user()