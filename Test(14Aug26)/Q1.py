"""
1. Create a Student Management System using Class and Object in Python. 
    What to Do:
        1. Create a class named Student.  
        2. Create a constructor __init__() to initialize:  
            o Student name  o Roll number  o Age  o Marks of 3 subjects  
        3. Create a display_details() method to display all student information.  
        4. Create a calculate_total() method to calculate the total marks.  
        5. Create a calculate_percentage() method to calculate the percentage.  
        6. Create a check_result() method:  
            o Student passes if marks in every subject are 35 or above.  
            o Otherwise, display FAIL.  
        7. Create an update_marks() method to update the marks of a selected subject.
"""

class Student:

    def __init__(self):
        self.name = " "
        self.roll = 0
        self.age = 0
        self.marks = {
            "English": 0,
            "Maths": 0,
            "Science": 0
        }

    def add_student(self):

        student = Student()

        student.name = input("Enter student name: ")
        student.roll = input("Enter roll no.: ")
        student.age = input("Enter age: ")

        for i in student.marks:
            student.marks[i] = int(
                input(f"Enter marks for {i}: ")
            )

        students.append(student)

        print("Student details saved successfully!")

        self.Menu()

    def display_details(self):

        user_roll = input(
            "Enter Roll No to see details of Student: "
        )

        for student in students:

            if student.roll == user_roll:

                print("\n___________ Student Details __________")

                print("Student Name:", student.name)
                print("Roll No:", student.roll)
                print("Age:", student.age)

                for i in student.marks:
                    print(i, ":", student.marks[i])

                self.Menu()
                return

        print("Invalid Roll No.")
        self.Menu()

    def calculate_total(self):

        user_roll = input(
            "Enter Roll No to see Total Marks: "
        )

        for student in students:

            if student.roll == user_roll:

                total = sum(student.marks.values())

                print("Total is:", total)

                self.Menu()
                return

        print("Invalid Roll No.")
        self.Menu()

    def calculate_percentage(self):

        user_roll = input(
            "Enter Roll No to see Percentage: "
        )

        for student in students:

            if student.roll == user_roll:

                total = sum(student.marks.values())
                percentage = total / len(student.marks)

                print("Percentage:", percentage, "%")

                self.Menu()
                return

        print("Invalid Roll No.")
        self.Menu()

    def show_result(self):

        user_roll = input(
            "Enter Roll No to see Result: "
        )

        for student in students:

            if student.roll == user_roll:

                if all(
                    mark >= 35
                    for mark in student.marks.values()
                ):
                    print("Result: PASS")
                else:
                    print("Result: FAIL")

                self.Menu()
                return

        print("Invalid Roll No.")
        self.Menu()

    def update_marks(self):

        user_roll = input(
            "Enter Roll No to update marks: "
        )

        for student in students:

            if student.roll == user_roll:

                print("\n1. English")
                print("2. Maths")
                print("3. Science")

                choice = int(
                    input("Enter subject choice: ")
                )

                if choice == 1:
                    student.marks["English"] = int(
                        input("Enter new English marks: ")
                    )

                elif choice == 2:
                    student.marks["Maths"] = int(
                        input("Enter new Maths marks: ")
                    )

                elif choice == 3:
                    student.marks["Science"] = int(
                        input("Enter new Science marks: ")
                    )

                else:
                    print("Invalid Subject Choice!")
                    self.Menu()
                    return

                print("Marks updated successfully!")

                self.Menu()
                return

        print("Invalid Roll No.")
        self.Menu()

    def Menu(self):

        print("\n1. Add Student Details.")
        print("2. Display Student Details.")
        print("3. Calculate Total.")
        print("4. Calculate Percentage.")
        print("5. Show Result.")
        print("6. Update Marks.")
        print("7. Exit.")

        ch1 = int(input("Enter Your Choice: "))

        match ch1:

            case 1:
                self.add_student()

            case 2:
                self.display_details()

            case 3:
                self.calculate_total()

            case 4:
                self.calculate_percentage()

            case 5:
                self.show_result()

            case 6:
                self.update_marks()

            case 7:
                self.exit()

            case _:
                print("Invalid Choice!")
                self.Menu()

    def exit(self):
        print("Thank You!")


# List to store all Student objects
students = []


# Create object
obj = Student()

# Start Menu
obj.Menu()