import json # it's very usefull for data read & write, speically when data in distionary formate, store the data
from datetime import datetime # use for automatic write in current date and time e.g.

customer_file = "customers.json"
log_file = "transactions.log"

def load_customer():
    try:
        with open(customer_file,"r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return{}

def save_customer(customers):
    with open(customer_file,"w") as f:
        json.dump(customers, f,indent=4)
        
def log_trasaction(massage):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {massage}\n")