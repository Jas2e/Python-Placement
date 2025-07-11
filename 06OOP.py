#class and object

class Car:
    def __init__(self,brand,model):#self: is context -means communicationline betweenobject ans class-
             self.brand=brand      #__init__- contructor- automatically called afte object creation
             self.model=model #instance

    def full_name(self):
        return f"{self.brand},{self.model}"         


my_car=Car("toyota","Corolla")

print(my_car.model)
print(my_car.full_name())


################## Inheritance #########################

class ElectricCar(Car):
    def __init__(self,brand,model,bettrySize):
        super().__init__(brand,model)
        self.bettrySize=bettrySize

my_tesla=ElectricCar("tesla","S","85K")

print(my_tesla.model)


######################## Encapulation ##################
# __brand - it make the brand variable or attribute private .

# only access by using getter method 
#  def get__brand(self):
#     retun self.__brand

########################### Polymorphism #####################

#Polymorphism via common interface(Duck Typing)
class NumberAdder:
    def add(self,a,b):
        return a+b

class StringAdder:
    def add(self,a,b):
        return a+b

#same interface :add()

def addition(adder,a,b):
    return adder.add(a,b)

numadder=NumberAdder()
stringadder=StringAdder()

print(addition(numadder,5,20))
print(addition(numadder,"5","20"))