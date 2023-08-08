class Car:
    total_cars = 0
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1

    def __str__(self):
        print("Make ",self.make)
        print("Model ",self.model)
        print("Year ",self.year) 

    def count(self):
        print(self.total_cars)       

obj = Car("Volvo","x",2016)
obj.__str__()
obj.count()
obj2 = Car("BMW","f",2015)
obj2.display()
obj2.count()