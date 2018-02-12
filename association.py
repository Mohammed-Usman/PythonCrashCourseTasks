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
        self.list_of_hardware = []

    def show_hardware(self,name,installed_date):

        self.list_of_hardware.append(name)
        self.list_of_hardware.append(installed_date)


class Software:

    def __init__(self):

        self.software_name = ''
        self.version = 0
        self.installed_date = ''
        self.list_of_software=[]

    def show_software(self,software_name,version,installed_date):

        self.list_of_software.append(software_name)
        self.list_of_software.append(version)
        self.list_of_software.append(installed_date)


class Computer:

    def __init__(self,name,manufacturer,location):

        self.name = name
        self.manufacturer = manufacturer
        self.location = location
        self.clasHadw = Hardware()
        self.clasSoft = Software()

    def setting_hardware(self):

        print('Setting Hardware',self.clasHadw.list_of_hardware)
        print()

    def setting_software(self):

        print('Setting Software',self.clasSoft.list_of_software)
        print()

    def list_of_hardware(self):

        print('List Of Hardware: ')

        for hadw_list in self.clasHadw.list_of_hardware:
            print(hadw_list)
        print()

    def list_of_software(self):

        print('List of Software: ')

        for soft_list in self.clasSoft.list_of_software:
            print(soft_list)
        print()

    def show_full_specification(self):

        print(self.name,self.manufacturer,self.location,'contains:')
        print(self.clasHadw.list_of_hardware)
        print(self.clasSoft.list_of_software)



comp = Computer('Usman-PC','DEll','Karachi')

comp.clasHadw.show_hardware('Lan Card','Feb 5')
comp.clasHadw.show_hardware('Graphic Card','Jan 18')
comp.clasHadw.show_hardware('DVD Rom','March 18')

comp.setting_hardware()
comp.list_of_hardware()

comp.clasSoft.show_software('Pycharm',2.4,'Dec 2')
comp.clasSoft.show_software('MS office',2016,'Aril 19')

comp.setting_software()
comp.list_of_software()

comp.show_full_specification()