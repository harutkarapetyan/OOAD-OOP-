        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def data(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")    
            
        
class Emploee(Person):
    def __init__(self, name, age, ID, departament):
        super().__init__(name, age)    
        self.ID = ID
        self.departament = departament
        
        
    def display_data(self):
        self.display()
        print(f"ID: {self.ID}, Departament {self.departament}")    
        
        
ob = Emploee("Jon", 25, 77071, 3)
ob.data("Jon",25)
ob.display_data()
