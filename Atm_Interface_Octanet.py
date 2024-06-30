class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((f"Deposit amount is:{amount}"))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            self.transactions.append((f"Withdraw amount is:{amount}"))
            return self.balance

    def get_transaction_history(self):
        return self.transactions if self.transactions else 'No transactions available'

    def transfer(self, target_account, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            self.transactions.append((f"Transfering amount is:{amount}"))
            return self.balance


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, pin, balance=0):
        self.accounts[user_id] = Account(user_id, pin, balance)

    def access_account(self):
        user_id = input("Enter your user ID:\n")
        pin = input("Enter your pin:\n")

        if user_id in self.accounts and self.accounts[user_id].check_pin(pin):
            return self.accounts[user_id]
        else:
            return None

    def run(self):
        while True:
            print("\nATM Interface")
            print("1. Access Account")
            print("2. Exit")
            choice = input("Choose an option:\n")
            if choice == '1':
                account = self.access_account()
                if account:
                    while True:
                        print("\n1. Transaction History")
                        print("2. Withdraw")
                        print("3. Deposit")
                        print("4. Transfer")
                        print("5. Exit")
                        operation = input("Choose an operation:\n")
                        if operation == '1':
                            print(account.get_transaction_history())
                        elif operation == '2':
                            amount = float(input("Enter withdraw amount:\n"))
                            print(account.withdraw(amount))
                        elif operation == '3':
                            amount = float(input("Enter deposit amount:\n"))
                            print(account.deposit(amount))
                        elif operation == '4':
                            target_id = input("Enter target user ID:\n")
                            amount = float(input("Enter amount to transfer:\n"))
                            if target_id in self.accounts:
                                print(account.transfer(self.accounts[target_id], amount))
                            else:
                                print("Target account not found.")
                        elif operation == '5':
                            break
                        else:
                            print("Invalid operation.")
                else:
                    print("Invalid user ID or pin.")
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")


atm = ATM()
atm.create_account('akash', '9766', 20000)
atm.create_account('vikas', '9552', 9000)
atm.run()

