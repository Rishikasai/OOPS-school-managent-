class Student:
      def __init__(self,listofstudents):
            self.availablestudents=listofstudents

      def displayAvailablestudents(self):
                   print("The students we have in our school are as follows:")
                   print("================================")
                   for student in self.availablestudents:
                        print(student)
      def removeStudent(self):
            print("Enter the name of the student you'd like to remove>>")
            self.removestudent=input()
            if self.removestudent in self.availablestudents:
                print("The student you requested has now been removed")
                self.availablestudents.remove(self.removestudent)
            else:
                print("Sorry the student you have requested is currently not in the school")
                  
      def addStudent(self):
            print("Enter the name of the student you'd like to add>>")
            self.newstudent=input()
            self.availablestudents.append(self.newstudent)
            print("The student",self.newstudent,"now has been added")

#INHERITANCE
class all(Student):
      def __init__(self,listofstudents,listofteachers):
            self.availableteachers=listofteachers
            Student.__init__(self,listofstudents)
      def displayAvailableteachers(self):
                   print("The students we have in our school are as follows:")
                   print("================================")
                   for student in self.availableteachers:
                        print(student)
class some:
      def __init__(self,listofstudents):
            self.availablestudents=listofstudents

      def displayAvailablestudents(self):
                   print("The students we have in our school are as follows:")
                   print("================================")
                   for student in self.availablestudents:
                        print(student)
      def __displayprotectedstudents(self):
                   print("The protected students are: ")
                   for student in self.availablestudents:
                        print(student)
def main():
      student=Student(["Harry","Ben"])
      All=all(["RAM","LAKSHMAN","BHARATH","SHATRAGN","SITA"],["Vashishta"])
      Some=some(["RAM","SITA"])
    
      done=False
      while done==False:
#ABSTRACTION
            print(""" ======SCHOOL MANAGEMENT======= 
                  1. Display all available students
                  2. Remove a student
                  3. add a student
                  4. Exit
                  5. Display Teachers
                  6. Show section A students (some) #Polymorphism
                  7. to show error for private students #Encapsulation
                  8. to show private students
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        All.displayAvailablestudents()
            elif choice==2:
                        All.removeStudent()
            elif choice==3:
                        All.addStudent()
            elif choice==4:
                  done=True
            elif choice==5:
                        All.displayAvailableteachers()
            elif choice==6:
                        Some.displayAvailablestudents()
            elif choice==7:
                        Some.displayprotectedstudents()
            elif choice==8:
                        Some._some__displayprotectedstudents()
          
main()
     
    
