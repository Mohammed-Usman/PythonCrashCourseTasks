class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.quizz='Quiz is pending'
        self.attendence='Present'
        self.fee='Paid'
        self.gpa=3.5

    def give_test(self):

        print('Name: ',self.name,'Roll Number:',self.roll_no,'\n'+self.quizz)

    def mark_present(self):

        print(self.name,'is',self.attendence)

    def pay_fee(self):
        print('Fee is ',self.fee)

    def homework(self):

        print(self.name,'do homework')

    def std_info(self):
        print("PARENT CLASS: ",self.name, 'have GPA', self.gpa,'\n')



stud1=Student('Usman',164)


stud1.give_test()
stud1.mark_present()
stud1.pay_fee()
stud1.homework()
stud1.std_info()



class TA(Student):

    def __init__(self,name,roll_no,teacher_name):
        super().__init__(name,roll_no)
        self.teacher_name=teacher_name

    def checking_assignment(self):
        print(self.name,'checks',self.teacher_name,'assignment')

    def std_info(self):
        self.gpa=3
        print("CHILD CLASS: ",self.name, 'have GPA', self.gpa,"assist's")


techr_assist=TA('Mahad',16,'Sir Zia')
techr_assist.checking_assignment()
techr_assist.std_info()

techr1_assist=Student('Usman',164)
techr1_assist.std_info()


