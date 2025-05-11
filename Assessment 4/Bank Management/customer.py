from file_handler import save_customer,log_trasaction,load_customer

# Withdrow Amount
def withdrow_amount(customers):
    acc_no = int(input("Enter Account Number : "))
    if acc_no in customers:
        amount = float(input("Enter Withdrow Amount : "))
        if amount <= customers[acc_no]["balance"]:
            customers[acc_no]["balance"] -= amount
            save_customer(customers)
            log_trasaction(f"{acc_no} Withdrow {amount}/-")
            print("Withdrow Amount Successcully..!")
        else:
            print("Insufficient Balance..!")
    else:
        print("Account Not Found..!")


# Deposite Amount
def deposite_amount(customers):
    acc_no = input("Enter Account Number : ")
    if acc_no in customers:
        amount = float(input("Enter Withdrow Amount : "))
        customers[acc_no]["balance"] += amount
        save_customer(customers)
        log_trasaction(f"{acc_no} Withdrow {amount}/-")
        print("Deposite Amount Successcully..!")
    else:
        print("Account Not Found..!")
        
        
# View Balance
def view_balance(customers):
    acc_no = input("Enter Account Number : ")
    if acc_no in customers:
        print(f"Current Balance : {customers[acc_no]['balance']}/-")
    else:
        print("Account Not Found..!")

def custer_menu():
    customers = load_customer()
    print("Welcome To Customer's App")
    print("\n\nOperation Menu")
    print("Press 1 --> Withdraw Amount")
    print("Press 2 --> Deposite Amount")
    print("Press 3 --> View Balanace")

    ch = input("Enter Your Choice : ")

    if ch == '1':
        withdrow_amount(customers)
    elif ch == '2':
        deposite_amount(customers)
    elif ch == '3':
        view_balance(customers)
    else:
        print("Operation Invalid..!")
custer_menu()
