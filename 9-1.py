class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type

    def open_resturant(self):
        print('The Resturtant is Open'.lower().title())


    def describe_resturant(self):
        print('Resturant Name is ',self.resturant_name.title(),'Cuisine',self.cuisine_type.title())

res=Resturant('a','v')
res.describe_resturant()
res.open_resturant()

