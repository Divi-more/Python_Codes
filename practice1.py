# Student Result System

# Enter student name and marks.
# Calculate total, percentage, grade.
# Display pass/fail.
# Add option to update marks.

class Student_Info:
    
    def __init__(self):
        self.name = " "
        self.marks ={
                     "English": 0, 
                     "Maths": 0,
                     "Physics": 0,
                     "Computer": 0,
                     "Science":0
                     }
        self.total = 0
        self.percentage = 0
        self.grade = ""
        self.result = ""
    
    def Menu(self):
        print("1. Enter student details. ")
        print("2. Calculate total, percentage, and grade. ")
        print("3. Display result. ")
        print("4. Update marks. ")
        print("5. Exit")
        
        ch = int(input("Enter Your choise: "))
        
        match ch:
            case 1:
                self.fill_details()
            
            case 2:
                self.calculate()
            
            case 3: 
                self.results()
            
            case 4:
                self.update_marks()
            
            case 5:
                self.exit() 
    
    def fill_details(self):
        self.name = input("Enter Student name: ")
        
        for subject in self.marks:
            self.marks[subject] = int(input(f"Enter makrs for: {subject}"))    
            
        print("Student details saved successfully !!!")   
        self.Menu()     
        
    def calculate(self):
        input_std = input("Enter student name to calculate marks:")
        if self.name == input_std:
            self.total = sum(self.marks.values())
            print("Total: ", self.total)
            self.percentage = self.total / len(self.marks)
            print("Percentage: ", self.percentage)
            
            if self.percentage >= 90:
                self.grade = "A"
            elif self.percentage >= 75:
                self.grade = "B"
            elif self.percentage >= 60:
                self.grade = "C"
            elif self.percentage >= 50:
                self.grade = "D"
            else:
                self.grade = "Fail"
            print("Grade: ", self.grade)
            self.Menu()
            
        else:               
            print("Enter Student details first. ")
            self.Menu()   
            
    def results(self):
        input_name = input("Enter a student name: ")
        
        if input_name == self.name:
            if all(mark >= 40 for mark in self.marks.values()):
                self.result = "Pass"
                print("Result is : ", self.result)
                self.Menu()
            else:
                self.result = "Fail"
                print("Result is: ", self.result)
                self.Menu()
        else:
            print("Invalid Student name.")
            self.Menu()
   
            
    def update_marks(self):
        input_name = input("Enter a student name: ")
        if input_name == self.name:
            for i in self.marks:
                self.marks[i] = int(input(f"Enter makrs for: {i}"))
            self.Menu()
        else:
            print("Invalid name")
            self.Menu()
                
    def exit(self):
        print("Thank You !")           
            
            
obj = Student_Info()
obj.Menu()            