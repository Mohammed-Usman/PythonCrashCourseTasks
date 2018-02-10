'''Association example
--Create a class Hardware with tow attributes 'name','installed_date'
and add a method show_hardware which will show name and date

--Create a class software with three attribute 'software_name','version','installed_date'
and a method SHOW_Software which will show name,version and date

--Create a class Computer with few attributes like 'name,'manufacture','location 'etc
and two attributes one for hardware and one for software
(list Type) and 5 function, for setting hardware,software,showing list of hardware,list of software and
Display full specifications of the computer
'''


class Hardware:
    def __init__(self):
        self.name = ''
        self.installed_date = ''
        self.nested_list_hardware = list()
        self.list_of_hardware = list()

    def show_hardware(self, name, installed_date):

        # print(name)
        # print(installed_date)

        if name:
            for i in range(1):
                self.list_of_hardware.insert(i,name)
                #print(self.list_of_hardware)
        return print(self.list_of_hardware)
        #return print('Length of', len(self.list_of_hardware))
        # self.list_of_hardware.append(installed_date)
        # print(self.nested_list_hardware.append(self.nested_list_hardware))
        # return self.nested_list_hardware.append(self.nested_list_hardware)


# hardware = Hardware()
# hardware.show_hardware()

class Software:
    def __init__(self):
        self.software_name = ''
        self.version = 0
        self.installed_date = ''
        self.list_of_software = []
        self.nested_list_software = []

    def show_software(self, software_name, version, installed_date):
        '''print(self.software_name)
        print(self.version)
        print(self.installed_date)'''

        self.list_of_software.append(software_name)
        self.list_of_software.append(version)
        self.list_of_software.append(installed_date)
        return self.nested_list_software.append(self.list_of_software)


# software=Software()
# software.show_software()



class Computer:
    def __init__(self):
        self.name = 'Usman-PC'
        self.manufacturer = 'Dell'
        self.location = 'Karachi'
        self.clasHadw = Hardware()
        self.clasSoft = Software()

    def setting_hardware(self, hard_name):
        # list return krao

        self.setHadw = []

    def setting_software(self, soft_name):
        # list return krao
        self.setSoft = []

    def list_of_hardware(self):
        for h in self.setHadw:
            print('Hardware List')

    def list_of_software(self):
        for s in self.setSoft:
            print('Software List')

    def show_full_specification(self):
        print('Show Full Specification')


'''comp=Computer()
comp.setting_hardware('DVD-ROM')
comp.setting_software('MS Office')
comp.list_of_hardware()
comp.list_of_software()
'''

comp = Computer()
comp1 = Computer()
print(comp.clasHadw.show_hardware('Lan Card', 'Feb 5'))
print(comp1.clasHadw.show_hardware('DVD Rom', 'Feb 5'))
comp.clasSoft.show_software('PyCharm', 2.4, 'Feb 6')

'''comp.setting_hardware('DVD-Rom')
comp.setting_software('Adobe')
comp.list_of_hardware()
comp.list_of_software()'''
