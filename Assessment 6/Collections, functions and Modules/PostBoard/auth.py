from data import *

def login():
    while True:
        username = (input("Enter Your Username : ")).strip()
        if username == "":
            print("User Can't Be Empty..!")
            continue
        role = (input("Enter Your Role : ")).strip().lower()
        if role not in ["user","staff"]:
            print("Inalid Role..!Select Role - 'user' or 'staff'")
            continue
        # store data into disctionary
        userdt = {
            "User_name" : username,
            "Role" : role
        }

        users.append(userdt)

        print(f"User_name : {username}\n Role : {role}")
        return userdt 
# login()