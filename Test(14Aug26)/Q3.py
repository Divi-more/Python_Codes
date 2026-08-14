"""
3. Create a simple Employee Management System using Class and Object in Python. 
    What to Do: 
        1. Create a class named Employee.  
        2. Create a constructor __init__() to initialize:  
                o Employee name  o Employee ID  o Department  o Basic salary  
        3. Create a display_details() method to display employee information.  
        4. Create a calculate_salary() method:  
            o Add a fixed bonus of ₹5,000.  
            o Calculate and display the final salary.  
        5. Create a check_salary() method:  
            o If salary is ₹30,000 or above, display "Good Salary".  
            o Otherwise, display "Average Salary".  
        6. Create a menu-driven program:  
            o 1 → Display Details  
            o 2 → Calculate Salary  
            o 3 → Check Salary  
            o 4 → Exit 
"""

class Employee:
    
    def __init__(self):
        self.emp_name = " "
        self.emp_ID = 0
        self.dept = " "
        self.salary = 0
    
    def Menu(self):
        print("1. Enter Employee Details.")
        print("2. Display Employee Details.")
        print("3. Calculate Salary.")
        print("4. Check Salary.")
        print("5. Exit.")
        
        ch = int(input("Enter Your Choise: "))
        
        match ch:
            
            case 1:
                self.add_emp()
            
            case 2:
                self.display_details()
            
            case 3:
                self.calculate_salary()
            
            case 4:
                self.check_salary()
            
            case 5:
                self.exit()
    
    def add_emp(self):
        emp = Employee()
        
        emp.emp_name = input("Enter Employee Name: ")
        emp.emp_ID = input("Enter Employee ID: ")
        emp.dept = input("Enter Employee Department: ")
        emp.salary = int(input("Enter Employee Salary: "))
        
        emps.append(emp)
        
        print("Employee Added !!!")
        self.Menu()
                
    
    def display_details(self):
        user_input = input("Enter Employee ID to see Details: ")
        
        for emp in emps:
            if emp.emp_ID == user_input:
                print("_____________Employee Details____________")
                print(f"Employee Name: {emp.emp_name}")
                print(f"Employee ID: {emp.emp_ID}")
                print(f"Department: {emp.dept}")
                print(f"Salary: {emp.salary}")
                self.Menu()
                return
        print("Invalid Employee ID.")
        self.Menu()    
    
    def calculate_salary(self):
        user_input = input("Enter Employee ID to calculate Salary: ")
        
        for emp in emps:
            if emp.emp_ID == user_input:
                final_salary = int(emp.salary) + 5000
                print(f"Basic Salary: {emp.salary}")
                print("Bonus: 5000")
                print(f"Total Salary: {final_salary}")
                self.Menu()
                return
        print("Invalid Employee ID.")
        self.Menu()
    
    def check_salary(self):
        user_input = input("Enter Employee ID to check Salary: ")
        
        for emp in emps:
            if emp.emp_ID == user_input:
                if emp.salary >= 30000:
                    print("Salary: ",emp.salary + 5000)
                    print("Your Salary is Good.")
                    self.Menu()
                    return
                print("Salary: ",emp.salary + 5000)
                print("Your salary is Average.")
                self.Menu()
                return
        print("Invalid Employee ID.")
        self.Menu()
        
    def exit(self):
        print("Thank You !")
    


emps = []
obj = Employee()
obj.Menu()    