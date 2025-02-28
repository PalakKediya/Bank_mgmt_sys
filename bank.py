import random
from report import GenerateReport

bank_accounts = []
all_Report = []


def search(acc_no):
    for i in range(len(bank_accounts)):
        if bank_accounts[i].acc_no == acc_no:
            return i
    else:
        return -1

# unique accnt no
def isunique_accnt(acc_no):
    if search(acc_no) != -1:
        print("Account all ready exist with same account no. please enter different account no.")
        acc_no = random.randint(1000, 9999)
        # acc_no = int(input("Enter a different account number: "))
        isunique_accnt(acc_no)  # This is not returning val
    else:
        return acc_no
    
# Method to deposit
def deposit():
    acc_no = float(input("Enter your account number : "))
    index = search(acc_no)
    if index != -1:
        amt_to_deposit = float(input("Enter the amount that you want to deposit : "))        
        bank_accounts[index].deposit(amt_to_deposit)
    else:
        print("Account does not exist !")

# Method for withdrawl
def withdraw():
    try:
        acc_no = int(input("Enter your account number: ").strip())  # Ensuring input is an integer
    except ValueError:
        print("Invalid input! Please enter a valid numeric account number.")
        return

    index = search(acc_no)
    if index != -1:
        try:
            amt_to_withdraw = int(input("Enter the amount that you want to withdraw: ").strip())
            if amt_to_withdraw <= 0:
                print("Withdrawal amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid numeric amount.")
            return

        bank_accounts[index].withdraw(amt_to_withdraw) 
    else:
        print("Account does not exist!")


# To check account details 
def check_acc_details():
    acc_no = int(input("Enter your Account number : "))
    index = search(acc_no)
    # print(index)
    if index != -1:
        bank_accounts[index].display()
    else:
        print("Account does not exist !")

# To check balance
def check_balance():
    acc_no = int(input("Enter your account number : "))
    index = search(acc_no)
    if index != -1:
        bank_accounts[index].checkbalance()
    else:
        print("Account does not exist !")

# To change status
def change_accnt_status():
    acc_no = int(input("Enter your account number : "))
    index = search(acc_no)
    if index != -1:
        bank_accounts[index].change_status()        
    else :
        print("Account does not exist !")

def generatereport():
    if not all_Report:
        print("No transactions available to generate a report.")
        return

    print("------------------------------------------------------------------------")
    print("Account No | Process                | Amount     | Balance")
    print("------------------------------------------------------------------------")
    
    for report in all_Report:
        print(report)

    print("------------------------------------------------------------------------")
