from bank import check_acc_details, deposit, withdraw, check_balance, change_accnt_status, generatereport, search, isunique_accnt, bank_accounts, all_Report
from report import GenerateReport
from saving import Savings
from salary import Salary
from current import Current
from loan import Loan
import random

# Main Menu
while True:
    print('------------------------------------------------------------------------')
    print("Press 1 to create a bank account")
    print("Press 2 to check account details")
    print("Press 3 to deposit money in an account")
    print("Press 4 to withdraw money from an account")
    print("Press 5 to check balance")
    print("Press 6 to close a bank account")
    print("Press 7 to change the status of your account")
    print("Press 8 to generate an end-of-day report")
    print("Press 0 to Exit")
    print('------------------------------------------------------------------------')
    
    choice = int(input("Enter your choice: "))
    print('------------------------------------------------------------------------')
    
    if choice == 1:
        print("Press 1 to create a Savings account")
        print("Press 2 to create a Salary account")
        print("Press 3 to create a Current account")
        print("Press 4 to create a Loan account")
        print('------------------------------------------------------------------------')
        
        acc_no = random.randint(1000, 9999)
        acc_no = isunique_accnt(acc_no)
        account_holder_name = input("Enter Account holder's name: ")
        
        acc_choice = int(input("Enter your choice: "))
        print('------------------------------------------------------------------------')
        
        if acc_choice == 1:
            while True:
                balance = float(input("Enter the balance amount: "))
                if balance >= Savings.avg_balance:
                    break
                else:
                    print("Balance must be at least 10,000!")
            
            acc = Savings(acc_no, account_holder_name, balance)
            bank_accounts.append(acc)
            all_Report.append(GenerateReport(acc_no, 'Saving Account created', balance,balance))
        
        elif acc_choice == 2:
            while True:
                balance = float(input("Enter the balance amount: "))
                if balance >= Savings.avg_balance:
                    break
                else:
                    print("Balance must be greater than the avg_balance, which is 10,000.")
            
            acc = Salary(acc_no, account_holder_name, balance, last_transaction_date='2024-12-5', status='Active')
            bank_accounts.append(acc)
        
        elif acc_choice == 3:
            balance = float(input("Enter the balance: "))
            acc = Current(acc_no, account_holder_name, balance, overdraft_amt=0.0, overdraft_limit=50000)
            bank_accounts.append(acc)
        
        elif acc_choice == 4:
            loan_taken = float(input("Enter the loan amount: "))
            balance = -loan_taken
            acc = Loan(acc_no, account_holder_name, loan_taken, balance, status='Active')
            bank_accounts.append(acc)
        
        else:
            print("Invalid choice! Please enter a valid option.")
        
        print("Account created successfully.")
        print(f"Please note down your Account number for future use: {acc_no}")
    
    elif choice == 2:
        check_acc_details()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        acc_no = int(input("Enter your Account number: "))
        index = search(acc_no)
        if index != -1:
            bank_accounts.pop(index)
            print("Account closed successfully!")
        else:
            print("Account does not exist!")
    elif choice == 7:
        change_accnt_status()
    elif choice == 8:
        generatereport()
    elif choice == 0:
        print("Program Finished!!!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
