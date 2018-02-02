def cars(manufacturer,model,**optional):
    car={}
    car['manufacturer']=manufacturer
    car['model']=model
    for k,v in optional.items():
        car[k]=v
    return car

a=cars('Suszuki',2017,color='green',type='Hybrid',tow_package=True)
print(a)
b=cars('HOnda',1986,color='WHITE',type='Car')
print(b)
c=cars('BMw',2015,color='green',type='Mini Truck',tow_package=False)
print(c)