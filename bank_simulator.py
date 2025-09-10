class bankaccount:
    def __init__(self, account_holder, pin, initial_balance=0):
        self.account_holder = account_holder
        self.pin = pin  
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print(" nvalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print(" invalid withdrawal amount!")

    def show_details(self):
        print("\n-- Account Details --")
        print(f" account holder: {self.account_holder}")
        print(f" account balance: {self.balance}")



accounts = {}


def create_account():
    name = input("Enter account holder name: ")
    pin = input("Set a 4-digit PIN: ")

    if not pin.isdigit() or len(pin) != 4:
        print(" invalid PIN! Must be 4 digits.")
        return

    initial_deposit = float(input("enter initial deposit amount: "))
    account = bankaccount(name, pin, initial_deposit)
    accounts[name] = account
    print(" Account created successfully!")


def access_account():
    name = input("enter account holder name: ")

    if name in accounts:
        pin = input("enter 4-digit PIN: ")
        account = accounts[name]

        
        if pin != account.pin:
            print(" incorrect PIN! Access denied.")
            return

        

        while True:
            print("\n-- Account Menu --")
            print("1. deposit")
            print("2. withdraw")
            print("3. show details")
            print("4. exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                print(" exiting account menu...")
                break
            else:
                print(" invalid choice! try again.")
    else:
        print(" account not found. please create an account first.")



while True:
    print("\n--  Bank Account Simulator --")
    print("1. create account")
    print("2. access account")
    print("3. exit")

    choice = input("enter your choice (1-3): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        access_account()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print(" invalid choice, please select a valid option.")
