class BankATM:
    
    def __init__(self):
        self.pin = " "
        self.balance = 0
    
    def Menus(self):
        print("1. Enter 1 to set PIN: \n")
        print("2. Enter 2 to Check balance: \n")
        print("3. Enter 3 to Deposite money: \n")
        print("4. Enter 4 to withdraw money: \n")
        print("5. Enter 5 to change PIN: \n")
        print("6. Enter 6 to Exit: \n")
        
        ch = int(input("Enter your Choise: "))
        
        match ch:
            case 1:
                self.set_pin()
            case 2:
                self.check_balance()
            case 3:
                self.deposit_money()
            case 4:
                self.withdraw_amount()
            case 5:
                self.change_pin()
            case 6:
                self.exit()
                
    def set_pin(self):
        if self.pin == " ":
            self.pin = input("Enter your pin")
            print("Pin is set: ", self.pin)
            self.Menus()
        else:
            print("PIN is already set.")  
            print("PIN: ", self.pin)  
            self.Menus()
            
    def check_balance(self):
        userpin = input("Enter your pin")
      
        if self.pin == userpin:
                print("Your Bank balance is : ",self.balance)
                self.Menus()
        else:
            print("Invalid pin.")
            self.Menus()
        
    def deposit_money(self):
        userpin = input("Enter your pin: ")
        
        if self.pin == userpin:
            input_amount = int(input("Enter amount for deposit: "))
            self.balance += input_amount
            print("Your current bank balance is: ", self.balance)
            self.Menus()
            
        else:
            print("Invalid pin.")
            self.Menus()
        
        
    def withdraw_amount(self):
        userpin = input("Enter your pin: ")
        
        if self.pin == userpin:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print("Your Remaining bank balance", self.balance)
                self.Menus()
            else:
                print("Insufficient balance.")
                self.Menus()
        else:
            print("Invalid pin.")
            self.Menus()
        
    def change_pin(self):
        userpin = input("Enter your old pin: ")
        
        if userpin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin updated: ", self.pin)
            self.Menus()
            
        else:
            print("Old in not matched. ")
            self.Menus()   
        
    def exit(self):
        print("Thank You ")    
        
obj1 = BankATM()
obj1.Menus()