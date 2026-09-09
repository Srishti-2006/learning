# create a system where user can create pin change pin see their balance and withdraw money
class Atm:
    def __init__(self):
        self.pin=' '
        self.balance=0

    def menu(self):
        user_input=input(""" 
        Hi how can i help you ?
        1. Press 1 to create pin.
        2. Press 2 to change pin.
        3. Press 3 to check balance.
        4.Press 4 to withdraw.
        5. Anything else to exit.
        """)

        if user_input=='1':
         self.create_pin()
        elif user_input=='2':
        #change pin
         self.change_pin()
        elif user_input=='3':
            #check balance
            self.check_balance()
        elif user_input=='4':
        #withdraw
         self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("enter your pin ")
        self.pin=user_pin

        user_balance=int(input("enter your balance"))
        self.balance=user_balance

        print("pin created successfullly")
        self.menu()

    def change_pin(self):
        old_pin=input("enter old pin")

        if old_pin==self.pin:
            #let him change the pin
            new_pin=input("enter new pin")
            self.pin=new_pin
            print(" pin change successful")
            self.menu()
        else:
            print("can't change")
            self.menu()
    def check_balance(self):
        print("your balance is:",self.balance)
        self.menu()


    def withdraw(self):
        user_withdraw_amount=int(input("enter amount to withdraw:"))
        self.withdraw=user_withdraw_amount
        self.balance-=user_withdraw_amount
        print("your account is debited by rs:",self.withdraw)
        print("your current balance is:",self.balance)
        self.menu()


atm1=Atm() 
atm2=Atm()
print(atm1.menu())
