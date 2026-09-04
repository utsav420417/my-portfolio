students = []

class Student:
    def __init__(self,student_id,name,rollno):
      self.student_id = student_id
      self.name = name
      self.rollno = rollno

    def Display(self):
        print(f"Id     : {self.student_id}")
        print(f"Name   : {self.name}")
        print(f"Rollno : {self.rollno}")
    

class CSITSTUDENT(Student):
   def display(self):
       super().Display()
       print("course:bsc csit")

n = int(input("Enter Range:"))

for i in range(n):
    
    student_id = int(input("please enter your Id:"))
    name = str(input("Enter student name: "))
    rollno = int(input("Enter Student rollno.:"))
    stu = CSITSTUDENT(student_id,name,rollno)
    students.append(stu)

for student in students:
  student.display()