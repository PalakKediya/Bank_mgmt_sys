from accounts import Account
class Current(Account):

    def __init__(self, acc_no, account_holder_name, balance, overdraft_amt, overdraft_limit ):
        super().__init__(acc_no, account_holder_name, balance)
        self.over_draft_limit = overdraft_limit
        self.over_draft_amount = overdraft_amt

    def display(self):
        super().display()
        print(f"Overdraft amount = {self.over_draft_amount}" )
        print(f"Overdraft limit = {self.over_draft_limit}" )

    def deposit(self, amt_to_deposit):
        if self.over_draft_amount > 0:
            if amt_to_deposit >= self.over_draft_amount:
                amt_to_deposit -= self.over_draft_amount
                print(f"Overdraft of amount {self.over_draft_amount} is repaid.")
                self.over_draft_limit += self.over_draft_amount
                self.over_draft_amount = 0
                self.balance = self.balance+amt_to_deposit
                print(f"By repaing all overdraft amount. Rupees {amt_to_deposit} is deposited in your account!")
                print(f"Current balance of your account is = {self.balance}")

            else:
                self.over_draft_amount -= amt_to_deposit
                self.over_draft_limit += amt_to_deposit
                print(f"Rs. {amt_to_deposit} overdraft amount is repaid. \nRemaining overdraft amount is {self.over_draft_amount}.")
        
        else:
            self.balance = self.balance+amt_to_deposit
            print(f"Rupees {amt_to_deposit} deposited in your account!")
            print(f"Current balance of your account is = {self.balance}")

    def withdraw(self, amt_to_withdraw):   

        if self.balance-amt_to_withdraw >= 0:
            self.balance = self.balance-amt_to_withdraw
            print(f"Rupees {amt_to_withdraw} WITHDRAWN from your account!")
            print(f"Current balance of your account is = {self.balance}")

        elif self.over_draft_limit >= 0:
            if (self.balance + self.over_draft_limit) >= amt_to_withdraw:
                overdraftneeded = amt_to_withdraw - self.balance
                self.over_draft_amount += overdraftneeded
                self.balance = 0
                self.over_draft_limit -= overdraftneeded
                print(f"Insufficient balance in your current accnt.")
                print(f"You will be taking rupees {overdraftneeded} as overdraft.")
                print(f"Rupees {amt_to_withdraw} WITHDRAWN from your account!")
                print(f"Current balance of your account is = {self.balance}")

            else:
                print("Insufficient balance... Overdraft limit reached")
                print(f"Current balance of your account is = {self.balance}")
                print(f"Over draft limit is = {self.over_draft_limit}")

    def checkbalance(self):
        return super().checkbalance()
    