class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type

    def open_resturant(self):
        print('The Resturtant is Open'.lower().title())


    def describe_resturant(self):
        print('Resturant Name is ',self.resturant_name,'Cuisine',self.cuisine_type.title())

a=Resturant('AAAA','aaa')
b=Resturant('BBB','bbb')
c=Resturant('CCC','ccc')

a.describe_resturant()
b.describe_resturant()
c.describe_resturant()

