from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, account_holder_name, balance):
        self.acc_no = acc_no
        self.acc_holder_name = account_holder_name
        self.balance = balance

    def display(self):
        print(f"Account Number = {self.acc_no}" )
        print(f"Account Holders Name = {self.acc_holder_name}" )
        print(f"Balance = {self.balance}" )
    
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass        

    def checkbalance(self):
        print(f"Balance in your account is {self.balance} ")