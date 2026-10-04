class Atm:

    def __init__(self):
        self.balance = 0
        self.pin ="1234"

        print("""
                what would you do with you bank account.
                1. create pin
                2. deposit 
                3. withdraw
                4. check balance 
        """)

    def check_balance(self):
        pin_code = input("Enter your pin")
        
        if(pin_code == self.pin):
            print("you current balance is:",self.balance)
        else:
            print("invalid pin")
        

    def deposit(self):
        pin = input("enter your pin")

        if(pin == self.pin):
            amount = int(input("enter you amount"))
            self.balance = self.balance + amount
            print("deposit succesfully")
        else:
            print("invalid pin")

cus = Atm()
