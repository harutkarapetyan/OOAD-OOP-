# class Employee:
#     employee_id = 1
#     def __init__(self,name):
#         self.name = name
#         self.emp_id = Employee.employee_id
        
        
#     def setdata(self,name):
#         self.name = name
            
#     def putdata(self):
#         return self.name, self.employee_id  
    
           
        
        
class Employee:
    employee_id = 1
    
    def __init__(self, name):
        self.name = name
        self.emp_id = Employee.employee_id
        Employee.employee_id += 1
        
        
    # def setdata(self, name):
    #     self.name = name
    #     self.emp_id = Employee.employee_id
    #     Employee.employee_id += 1
        
    def putdata(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
  
obj1 = Employee("John")
obj1.putdata()
obj2 = Employee("James")
obj2.putdata()