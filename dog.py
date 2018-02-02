class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")
        print(self.name.title(),'is ',self.age,'year old')

    def roll_over(self):
        print(self.name.title() + " rolled over!")
        print(self.name.title(), 'is ', self.age, 'year old')


my_dog = Dog('doggy', 6)
your_dog=Dog('lucy',5)
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()