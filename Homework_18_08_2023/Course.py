""" Course    """
class Course:
    def __init__(self, name_course, credit_course):
        self.name_course = name_course
        self.credit_course = credit_course
        self.students = []
        
    def add_student(self, name_student):
        self.students.append(name_student)
        
    def display(self):
        print(f"Course: {self.name_course}\nCredit: {self.credit_course}")
        for i in self.students:
            print("Student:",i)

class Departament:
    def __init__(self):
        self.Courses = {}
          
    def add_course(self, course_name,credit_course):
        course = Course(course_name,credit_course)
        self.Courses[course_name] = course
        
    def add_student_to_course(self,student, course_name):
        if course_name in self.Courses:
            self.Courses[course_name].add_student(student)
        else:
            print("Course not found") 
                
    def display_full(self):
        print("--DEPARTAMENT--")
        for _, i in self.Courses.items():
            i.display()
            
obj = Departament()

obj.add_course("Matem",6)
obj.add_student_to_course("Armen","Matem")

obj.add_course("Fizika",3)

obj.add_student_to_course("Viliam","Fizika")
obj.add_student_to_course("Armen","Fizika")

obj.display_full()                         
                      