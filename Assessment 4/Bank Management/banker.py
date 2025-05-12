from datetime import datetime # It Get the correct date and time & it also store it with customer data or in logs.
from file_handler import save_customer, log_trasaction,load_customer

customers = load_customer() # create disctionary for customer, using to stores the records of all customer

# here, we write the code for add to customer
def add_customer():
    acc_no = int(input("Enter Account Number : "))
    if acc_no in customers:
        print("Account Already Exists")
    else:
        name = input("Enter Customer Name : ")
        balance = float(input("Enter Opening Balance : "))
        open_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        customers[acc_no] = {"Name":name,"Balace":balance,"Opening Date":open_date}
        save_customer(customers)
        log_trasaction(f"Add Customer : {acc_no} - {name}")
        print("Recorded Inserted Successfully.....!")
    
# then, view specific customer according to the user
def viwe_customer():
    acc_no = input("Enter a account number to view : ")
    if acc_no in customers:
        print(f"Account Number : {acc_no}\n Details : {customers[acc_no]}")
    else:
        print(f"We can't find this {acc_no} please chek the customer accounts..!")
        
# Search the customer
def search_customer():
    search_name = input("Enter Customer Name : ")
    status = False
    for acc_no,detail in customers.items():
        if detail["Name"].lower() == search_name.lower():
            print(f"Account Number : {acc_no}\n Details : {detail}")
            status = True
    if not status:
        print(f"We can't find this {search_name} please chek the customer accounts..!")
        
# View all customer
def view_all_customer():
    if not customers:
        print("No Cutomer Record Found..!")
    for acc_no,detail in customers.items():
        print(f"Account Number : {acc_no}\n Details : {detail}")
        
# total amount in bank
def total_amout():
   total = sum(detail['Balace'] for detail in customers.values())
   print(f"Total balance in bank : {total}")

# make banker_menu 
def banker_menu():
    while True:
        print("Welcome To Banker's App")
        print("Press 1 --> Add Customer")
        print("Press 2 --> View Cutomer")
        print("Press 3 --> Search Cutomer")
        print("Press 4 --> View All Cutomer")
        print("Press 5 --> Total Amount In Banks")

        ch = input("Enter Your Choice : ")

        if ch == '1':
            add_customer()
        elif ch == '2':
            viwe_customer()
        elif ch == '3':
            search_customer()
        elif ch == '4':
            view_all_customer()
        elif ch == '5':
           total_amout()
        else:
            print("Invalid Choice")
