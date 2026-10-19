class BankAccount:

    def __init__(self):
        self.__balance = 0.0


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")


    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")
 


    def check_balance(self):
        print("you current balance is :",self.__balance)


    def get_balance(self):
        return self.__balance



class Atm(BankAccount):

    def __init__(self):
        super().__init__()
        self.__pin ="1234"


    def set_pin(self):
        pin = input("enter you pin")
        self.__pin = pin 
        print("pint set successfully")


    def verify_pin(self):
        pin = input("Enter your PIN: ")
        return pin == self.__pin
        

    def check_balance(self):
        
        if self.verify_pin():
            super().check_balance()
        else:
            print("invalid pin")
        

    def deposit(self):
        if self.verify_pin():
            amount = int(input("enter you amount"))
            super().deposit(amount)
            

    def withdraw(self):
        if self.verify_pin():
            amount = int(input("enter your amount"))
            super().withdraw(amount)


cus = Atm()   

while True:
    print("""
        1. Set PIN
        2. Deposit
        3. Withdraw
        4. Check balance
        5. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        cus.set_pin()
    elif choice == "2":
        cus.deposit()
    elif choice == "3":
        cus.withdraw()
    elif choice == "4":
        cus.check_balance()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
