from accounts import Account

class Loan(Account):
    def __init__(self, acc_no, account_holder_name, loan_taken, balance, status):
        super().__init__(acc_no, account_holder_name, balance)
        self.loan_taken = loan_taken
        self.status = status

    def display(self):
        super().display()
        print(f"Loan Amount: {self.loan_taken}")
        print(f"Account Status: {self.status}")

    def deposit(self, amount):
        if self.status != 'Active':
            print("Your account is CLOSED! You cannot deposit money as you have repaid your loan.")
            return
        
        self.balance += amount  # Always update the balance

        print(f"Deposited {amount} successfully.")
        print(f"Current Balance: {self.balance}")

        if self.balance >= 0:  # If the loan is fully paid or overpaid
            self.status = 'Closed'
            print("Your loan is fully repaid. Account is now closed.")


    def withdraw(self, amount):
        print("Withdrawals are not allowed from a loan account.")

    def check_balance(self):
        return self.balance