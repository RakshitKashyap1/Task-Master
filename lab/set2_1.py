class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer({self.customer_id}): {self.name}"


class Account:
    def __init__(self, account_number, customer, balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f"Account({self.account_number}) - "
                f"Owner: {self.customer.name}, Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print(f"Added customer: {customer}")
        else:
            print(f"Customer ID {customer.customer_id} already exists.")

    def open_account(self, customer, initial_deposit=0.0):
        if customer.customer_id not in self.customers:
            print(f"Customer {customer.name} does not exist. Please add the customer first.")
            return None

        # Generate a unique account number (for simplicity, using len(accounts) + 1)
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, customer, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Opened account {account_number} for {customer.name} with initial deposit of ${initial_deposit:.2f}")
        return new_account

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def __str__(self):
        return f"Bank({self.name}) - {len(self.accounts)} accounts, {len(self.customers)} customers"


def main():
    my_bank = Bank("MyBank")

    while True:
        print("\n--- Bank Management System ---")
        print("1. Add Customer")
        print("2. Open Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Display Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            customer_id = input("Enter customer ID: ")
            customer = Customer(name, customer_id)
            my_bank.add_customer(customer)

        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            if customer_id in my_bank.customers:
                customer = my_bank.customers[customer_id]
                initial_deposit = float(input("Enter initial deposit amount: "))
                my_bank.open_account(customer, initial_deposit)
            else:
                print("Customer not found. Please add the customer first.")

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            account = my_bank.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            account = my_bank.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            account_number = int(input("Enter account number: "))
            account = my_bank.get_account(account_number)
            if account:
                print(f"Balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == '6':
            print("\nAccounts:")
            for account in my_bank.accounts.values():
                print(account)

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()