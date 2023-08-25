class Project:
    def __init__(self, name_project, description):
        self.name_project = name_project
        self.description = description
        self.employees = []
        
    def add_employee(self, name_employee):
        self.employees.append(name_employee)
        
    def display(self):
        print(f"Name_project: {self.name_project}\nDescription: {self.description}")
        for i in self.employees:
            print("Name_enployee:", i)
            
            
class Company:
    def __init__(self):
        self.projects = {}
        
    def create_project(self,name_project,description):
        project = Project(name_project,description)
        self.projects[name_project] = project
    
    def add_employee_to_project(self, name_employee, name_project):
        if name_project in self.projects:
            self.projects[name_project].add_employee(name_employee) 
        
        
    def display_projects(self):
        print("Company project")
        for _, project in self.projects.items():
            project.display()    
                            
            
com = Company()
com.create_project("A","For loop")
com.create_project("B","For you")

com.add_employee_to_project("Bony","A")
com.display_projects()    