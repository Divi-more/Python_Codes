"""
2. Create a Library Management System using Class and Object in Python. 
    What to Do:
        1. Create a class named Book.  
        2. Create a constructor __init__() to initialize:  
            o Book name  o Book ID  o Author name  o Availability status  
        3. Create a display_book() method to display book details.  
        4. Create a issue_book() method:  
            o Check whether the book is available.  
            o If available, issue the book and change its status.  
            o If already issued, display an appropriate message.  
        5. Create a return_book() method:  
            o Return the issued book.  
            o Change its availability status back to available.  
        6. Create a check_availability() method to display whether the book is available or issued. 
"""

class Book:
    def __init__(self):
        self.bookname = " "
        self.bookid = 0
        self.authorname =" "
        self.availability = " "
        
    def Menu(self):
        print("1. Add Book Details.")
        print("2. Display Book Details.")
        print("3. Issue book.")
        print("4. Return book.")
        print("5. Check availability.")
        print("6. Exit.")
        
        ch = int(input("Enter your choise: "))
        
        match ch:
            
            case 1:
                self.add_book()
            
            case 2:
                self.display_book()
            
            case 3:
                self.issue_book()
            
            case 4:
                self.return_book()
            
            case 5:
                self.check_availability()
            
            case 6:
                self.exit()
        
    def add_book(self):
        book = Book()
        
        book.bookname = input("Enter Book name: ")
        book.bookid = input("Enter book id: ")
        book.authorname = input("Enter author name: ")
        book.availability = input("Enter if Available or Not? : ")
        
        Book1.append(book)
        
        print("Book Added !!!")
        self.Menu()
        
    def display_book(self):
        user_input = input("Enter Book ID to see all Details: ")
        
        for book in Book1:
            if book.bookid == user_input:
                
                print("_______________Book Details_____________")
                
                print("Book Name: ", book.bookname)
                print("Book ID: ", book.bookid)
                print("Author Name: ", book.authorname)
                print("Is Book Available? : ", book.availability)
                
                self.Menu()
                return
        print("Invalid Book ID.")
        self.Menu()
    
    def issue_book(self):
        user_input = input("Enter Book ID to issue Book: ")
        
        for book in Book1:
            if book.bookid == user_input:
                if book.availability == "Yes":
                    print("Book has been issued. ")
                    book.availability = "Not"
                else:
                    print("Book is not Available. ")
                self.Menu()

        print("Invalid Book ID")
        self.Menu()
        return
    
    def return_book(self):
        user_input = input("Enter Book ID to return the Book to Library: ")
        
        for book in Book1:
            if book.bookid == user_input:
                if book.availability == "Not":
                    book.availability = "Yes"
                    print("The Book has been returned.")
                else:
                    print("The Book has not been Issued.")
                self.Menu()
                return
            
            
        print("Invalid Book ID.")
        self.Menu()
        return    
    
    def check_availability(self):
        user_input = input("Enter Book ID to see if Book is Available or Not? : ")
        
        for book in Book1:
            if book.bookid == user_input:
                if book.availability == "Yes":
                    print("Book is Available.")
                else:
                    print("Book is NOT Available.")
                
                self.Menu()
                return
            
        self.Menu()
        return
                
    def exit(self):
        print("Thank You !")
        
        
    
Book1 = []

obj = Book()
obj.Menu()
