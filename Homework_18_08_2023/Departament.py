class Departament:
    def __init__(self, departament_name):
        self.departament_name = departament_name
        self.employees = []
    
    def add_employee(self, employee_name):
        self.employees.append(employee_name)
        
    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            self.employees.remove(employee_name)
        else:
            print("Employee not found")    
        
        
        
    def display(self):
        print("Departament_name:",self.departament_name)
        for i in self.employees:
            print("Employee_name:", i)
            
class Company:
    def __init__(self):
        self.departaments = {}
        
    def create_departament(self, departament_name):
        departament = Departament(departament_name)
        self.departaments[departament_name] = departament
        
    def add_employee_to_departament(self,employee_name, departament_name):
        if departament_name in self.departaments:
            self.departaments[departament_name].add_employee(employee_name)
        else:
            print("Departament not found")
            
    def remove_employee_to_departament(self,employee_name, departament_name):
        if departament_name in self.departaments:
            self.departaments[departament_name].remove_employee(employee_name)
        else:
            print("Departament not found")
            
    def display_departament(self):
        print("  --DEPARTAMENTS--  ")
        for _,i in self.departaments.items():
            i.display()
            
            
obj = Company()

obj.create_departament("Volvo")
obj.add_employee_to_departament("VALOD","Volvo")           
obj.create_departament("BMW")
obj.add_employee_to_departament("KARO","BMW")  
obj.display_departament()      
obj.remove_employee_to_departament("KARO","BMW")   
obj.display_departament()        
                  