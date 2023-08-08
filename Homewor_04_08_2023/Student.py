class Student:
    def __init__(self,name,age,id):
        self.__id = id
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value >= 0:
            self.__age = value
        else:
             print("Age cannot be negative.")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 0:
            self.__name = value
        else:
            print("Name cannot be empty.")    

    
obj = Student("Jems",25,29)
print(obj.__id) 
'''AttributeError'''
print(obj.age) 
print(obj.name) 

