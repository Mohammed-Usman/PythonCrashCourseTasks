class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        print('First Name: ',self.first_name)
        print('Lasr Name: ',self.last_name)
        print('Age is: ',self.age)
        print('Gender is: ',self.gender)

    def greet_user(self):

        print('Hello',self.first_name,'\n')


first_person=User('Muhammad','Usman',22,'M')
second_person=User('Hassan','ALi',18,'M')
third_person=User('Shaemeela','Farooqi',42,'M')

first_person.describe_user()
first_person.greet_user()

second_person.describe_user()
second_person.greet_user()

third_person.describe_user()
third_person.greet_user()
