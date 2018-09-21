class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type

    def open_resturant(self):
        print('The Resturtant is Open'.lower().title())


    def describe_resturant(self):
        print('Resturant Name is ',self.resturant_name.title(),'Cuisine',self.cuisine_type.title())

res=Resturant('Lal-Qila','Desi')
res.describe_resturant()
res.open_resturant()

class Ice_Cream_Stand(Resturant):

    def __init__(self,resturant_name,cuisine_type):
        super().__init__(resturant_name,cuisine_type)
        self.flavors=['vanila','chocolate','strawberry','melon','fanta']

    def display_flavors(self):
        print(self.resturant_name)
        for flv in self.flavors:
            print('Flavors are: ',flv)


flv1=Ice_Cream_Stand('Move-n-Pick','Chinese')
flv1.describe_resturant()
flv1.display_flavors()