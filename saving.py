from accounts import Account

class Savings(Account):

    avg_balance = 10000
    
    def __init__(self, acc_no, account_holder_name, balance):
        super().__init__(acc_no, account_holder_name, balance)

    def display(self):
        super().display()

    def deposit(self, amt_to_deposit):
        self.balance = self.balance+amt_to_deposit
        print(f"Rupees {amt_to_deposit} deposited in your account!")
        print(f"Current balance of your account is = {self.balance}")

    def withdraw(self, amt_to_withdraw):    
        if self.balance-amt_to_withdraw >= Savings.avg_balance:
            self.balance = self.balance-amt_to_withdraw
            print(f"Rupees {amt_to_withdraw} withdrawn from your account!")
            print(f"Current balance of your account is = {self.balance}")
        else:
            print('Insufficient balance')
            
    def checkbalance(self):
        return super().checkbalance()   