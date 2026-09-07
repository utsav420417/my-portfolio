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
    

class CSITSTUDENT(Student):   #inheritance
   def display(self):         #function constructure
       super().Display()      #acces properties of function constructure
       print("course:bsc csit")

def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please Enter a valid Number")

while True:
      print("\n===STUDENT MANAGEMENT SYSTEM===")
      print("1. Add Student")
      print("2. Display Students")
      print("3. Search Student")
      print("4.Delete Students")
      print("5. Update Student")
      print("6. Exit")

      Choice = get_integer('Enter Choice : ')


      if Choice == 1:
         print("Add Student")
         n = int(input("enter range"))
         for i in range(n):             
             student_id = get_integer("Enter Student ID")
             id_exist = False
             for student in students:
                 if student.student_id == student_id:
                     id_exist = True
                     break
                 if id_exist:
                  print(f"Student Id({student_id}alreadyy exit)")
                     
             else:
                 name = input("Enter Student Name: ")
                 rollno = get_integer("Enter Roll No.: ")

                 stu = CSITSTUDENT(student_id,name,rollno)
                 students.append(stu)
                 print("student Added Sucesfully")
       
      elif Choice == 2: 
         print("Display student")

         if len(students) == 0:
             print("no student found")
         else:
            for student in students:
               student.display()
 
      elif Choice == 3:
           print("Search Student")
      
         
           Search_id = get_integer("Enter Student ID")
           found = False

           for student in students:
              if student.student_id == Search_id:
                 student.display()
                 found = True
                 break
              if not found:
                  print("No Student found")

      elif Choice == 4:
            print("Delete Students")
            
            
            delete_id = get_integer("Enter Student ID to Delete")
            
            for student in students:
               if student.student_id == delete_id:
                 students.remove(student)
                 print("student deleted sucessfully")
                 break

            else:
               print("student not found")
         
      elif Choice == 5:  
          print("Ubdate Student")

          update_id = get_integer("Enter Student ID")

          found = False

          for student in students:
              if student.student_id == update_id:
                  print("Studdent Found")
                  student.name = input("Enter Student Name")
                  student.rollno = get_integer("Enter Rollno.:")

                  print("Student Update sucessfully")
                  found = True
                  break
          if not found:
            print("Student Not Found")
            
      elif Choice == 6:
          print("GoodByee")
          break
             
      else:
          print("Invalid Choice")
            

