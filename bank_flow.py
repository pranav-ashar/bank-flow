#Storing of initial customer details

bank_records = {
    123456789101 : 
    {
        "name" : "Charlie Chaplin",
        "pin" : 1889,
        "balance" : 10000,
        "transactions" : []
    },
    
    123456789102 : 
    {
        "name" : "Napoleon Bonaparte",
        "pin" : 1769,
        "balance" : 120000,
        "transactions" : []
    },
    
    123456789103 : 
    {
        "name" : "Adolf Hitler",
        "pin" : 1889,
        "balance" : 500000,
        "transactions" : []
    },
    
    123456789104 : 
    {
        "name" : "William Shakespeare",
        "pin" : 1564,
        "balance" : 5000,
        "transactions" : [] 
    },
    
    123456789105 : 
    {
        "name" : "Pablo Escobar",
        "pin" : 1949,
        "balance" : 1000000,
        "transactions" : []
    }
}


            
def login():
    while True:
        global account_num
        account_num = int(input("Enter Account Number : "))
        if account_num in bank_records:
            
            print()
            print(f"Welcome, {bank_records[account_num]["name"]}")
            print()
            menu(account_num)
            
            
        else:
            print("Invalid Account Number")
            print()


#Account Balance
def acc_bal(acc_no):
    acc_no = account_num
    
    print("-------------------")
    print("ACCOUNT BALANCE")
    print(f"{bank_records[acc_no]["name"]}")
    print(f"Balance : $ {bank_records[acc_no]["balance"]}")
    print("-------------------")
    operation()

#Deposit
def deposit(acc_no):
    print("-------------------")
    deposit_amt = int(input("Enter Amount : "))
    if (deposit_amt > 0):
        balance_new = (bank_records[acc_no]["balance"]) + deposit_amt
        bank_records[acc_no].update({"balance" : balance_new})
        bank_records[acc_no]["transactions"].append(f"Deposited : + ${deposit_amt}")
        print(f"The Amount of $ {deposit_amt} is added succesfully to your account")
        print("-------------------")
        
        operation()
    else:
        print("Invalid Amount Entered")
        print("-------------------")
    
#Withdrawl    
def withdraw(acc_no):
    print("-------------------")
    withdrawl_amt = int(input("Enter Amount : "))
    balance_new = (bank_records[acc_no]["balance"]) - withdrawl_amt
    if (balance_new >= 500):
        bank_records[acc_no].update({"balance" : balance_new})
        print(f"The Amount of $ {withdrawl_amt} has succesfully withdrawn from your account")
        print("-------------------")
        operation()
    else:
        print("Insufficient Balance")
        print("-------------------")
    
#Pin Change
def pin_change(acc_no):
    print("-------------------")
    prev_pin = int(input("Enter Previous Pin : "))
    if(prev_pin == bank_records[acc_no]["pin"]):
        new_pin = input("Enter New Pin : ")
        bank_records[acc_no].update({"pin" : new_pin})
        print("The Pin has been Updated")
        print("-------------------")
        operation()
    else:
        print("Invalid Pin")
        print("-------------------")

#Transfer Money
def transfer_money(acc_no):
    transfer_acc = int(input("Enter Account Number of Trasnsferee : "))
    if transfer_acc in bank_records:
        print(f"Account holder Name : {bank_records[transfer_acc]["name"]}")
        transfer_amt = int(input("Enter Amount to Transfer : "))
        if (transfer_amt > 0):
            balance_new_trasferee = bank_records[transfer_acc]["balance"] + transfer_amt
            balance_new_transferer = bank_records[acc_no]["balance"] - transfer_amt
            if(balance_new_transferer >= 500):
                bank_records[transfer_acc].update({"balance":balance_new_trasferee})
                bank_records[acc_no].update({"balance":balance_new_transferer})
                print(f"The amount of $ {transfer_amt} has been transferred to {bank_records[transfer_acc]["name"]}")
                print()
                operation()
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Amount")
    else:
        print("Incorrect Account Number")

# Mini Statement
def mini_statement(acc_no):
    print("-------------------")
    print("MINI STATEMENT")
    for item in bank_records[acc_no]["transactions"]:
        print(item)
    print("-------------------")
    operation()

#Menu
def menu(acc_no):
    acc_no = account_num
    print("""-------ATM-------
1) Check Balance
2) Deposit Money 
3) Withdraw Money 
4) Transfer Money
5) Mini Statement
6) Change Pin 
7) Logout
-----------------
""")
    user_response = int(input("User Response : "))
    print()
    if(user_response == 1):
        acc_bal(acc_no)
    elif(user_response == 2):
        deposit(acc_no)
    elif(user_response == 3):
        withdraw(acc_no)
    elif(user_response == 4):
        transfer_money(acc_no)
    elif(user_response == 5):
        mini_statement(acc_no)
    elif(user_response == 6):
        pin_change(acc_no)
    elif(user_response == 7):
        logout()
    else:
        print("Invalid Response")
    
        
def operation():
    
    print("""
Would you like another transaction?

1) Yes
2) Logout """)
    print()
    user_response = int(input("User Response : "))
    if(user_response == 1):
        print()
        menu(account_num)
    elif(user_response == 2):
            print()
            logout()
    else:
        print("Invalid Response")
        
def logout():
    login()
        
        

#Program Run

login()



