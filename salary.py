from saving import Savings
from datetime import date, datetime

class Salary(Savings):

    def __init__(self, acc_no, account_holder_name, balance, last_transaction_date, status):
        super().__init__(acc_no, account_holder_name, balance)
        self.last_transaction_date = last_transaction_date
        self.status = status

    def display(self):
        super().display()
        print(f"Last Transaction Date = {self.last_transaction_date}" )
        print(f"Status = {self.status}")

    def deposit(self, amt_to_deposit):
        super().deposit(amt_to_deposit)
    
    def withdraw(self, amt_to_withdraw):    
        if self.status != 'Frozen':
            now = date.today()
            if isinstance(self.last_transaction_date, str):
                last_tr_date = datetime.strptime(self.last_transaction_date,'%Y-%m-%d').date()
            else:
                last_tr_date = self.last_transaction_date
            difference = abs((last_tr_date - now).days)
            if difference < 60 :
                super().withdraw(amt_to_withdraw)
                self.last_transaction_date = (date.today())
            else:
                self.status = 'Frozen'
                print("Your Account is freezed as there is no transaction done in LAST 60 DAYS (2 MONTHS). \nTo Withdraw money you need to make you accont Active by paying FINE of rupees 100 !!!")
        else:
            print("Your account is 'Freezed' because there is no transaction done from last 2 Months.\nTo Withdraw money you need to make you accont Active by paying FINE of rupees 100 !!!")
        
    def checkbalance(self):
        return super().checkbalance()
     
    def change_status(self):
        if self.status == 'Frozen':
            if self.balance - 100 > Savings.avg_balance:
                self.balance -= 100
                self.status = 'Active'
                self.last_transaction_date = date.today()
                print("Your account is REACTIVATED! \nFine of 100 rupees deducted from your account...")
            else:
                print("Inusufficient Balance")
        else:
            print("Your account is already Active!")
