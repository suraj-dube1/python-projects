class Atm:

    def __init__(self):
        self.__balance = 0
        self.__pin ="1234"

        print("""
                what would you do with you bank account.
                1. Set pin
                2. get pin
                3. set pin
                4. deposit 
                5. withdraw
                6. check balance 
        """)

    def set_pin(self):
        pin = input("enter you pin")
        self.__pin = pin 
        print("pint set successfully")
        

    def get_pin(self):
        print(self.__pin)


    def check_balance(self):
        pin_code = input("Enter your pin :")
        
        if(pin_code == self.__pin):
            print("you current balance is :",self.__balance)
        else:
            print("invalid pin")
        

    def deposit(self):
        pin = input("enter your pin :")

        if(pin == self.__pin):
            amount = int(input("enter you amount"))
            self.__balance = self.__balance + amount
            print("deposit succesfully")
        else:
            print("invalid pin")
            

    def withdraw(self):
        pin = input("enter you pin")

        if (self.__pin == pin):
            amount = float(input("enter your amount"))
            if amount > self.__balance:
                print("invalid amount")
            else:
                self.__balance = self.__balance - amount
                print("withdraw succesfully")


cus = Atm()   
data = int(input("enter your choice"))

if(data == 1):
    cus.set_pin()
elif(data == 2):
    cus.get_pin()
elif(data == 3):
    cus.deposit()
elif(data == 4):
    cus.withdraw()