#Storing of initial customer details

bank_records = {
    123456789101 : 
    {
        "name" : "Charlie Chaplin",
        "pin" : 1889,
        "balance" : 10000
    },
    
    123456789102 : 
    {
        "name" : "Napoleon Bonaparte",
        "pin" : 1769,
        "balance" : 120000
    },
    
    123456789103 : 
    {
        "name" : "Adolf Hitler",
        "pin" : 1889,
        "balance" : 500000
    },
    
    123456789104 : 
    {
        "name" : "William Shakespeare",
        "pin" : 1564,
        "balance" : 5000
    },
    
    123456789105 : 
    {
        "name" : "Pablo Escobar",
        "pin" : 1949,
        "balance" : 1000000
    }
}

#Account Balance
def acc_bal(acc_no):
    print("ACCOUNT BALANCE")
    print(f"{bank_records[acc_no]["name"]}")
    print(f"Balance : $ {bank_records[acc_no]["balance"]}")

#Deposit
def deposit(acc_no):
    deposit_amt = int(input("Enter Amount : "))
    if (deposit_amt > 0):
        balance_new = (bank_records[acc_no]["balance"]) + deposit_amt
        bank_records[acc_no].update({"balance" : balance_new})
        print(f"The Amount of $ {deposit_amt} has added succesfully to your account")
        print()
    else:
        print("Invalid Amount Entered")
    
#Withdrawl    
def withdrawl(acc_no):
    withdrawl_amt = int(input("Enter Amount : "))
    balance_new = (bank_records[acc_no]["balance"]) - withdrawl_amt
    if (balance_new >= 500):
        bank_records[acc_no].update({"balance" : balance_new})
        print(f"The Amount of $ {withdrawl_amt} has succesfully withdrawn from your account")
        print()
    else:
        print("Insufficient Balance")
    
#Pin Change
def pin_change(acc_no):
    prev_pin = int(input("Enter Previous Pin : "))
    if(prev_pin == bank_records[acc_no]["pin"]):
        new_pin = input("Enter New Pin : ")
        bank_records[acc_no].update({"pin" : new_pin})
        print("The Pin has been Updated")
    else:
        print("Invalid Pin")

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
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Amount")
    else:
        print("Incorrect Account Number")





