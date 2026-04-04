# auth.py

from data import users

def login():
    while True:
        username = input("Enter Your Username: ").strip()

        if username == "":
            print("Username can't be empty!")
            continue

        role = input("Enter Your Role (user/staff): ").strip().lower()

        if role not in ["user", "staff"]:
            print("Invalid Role! Choose 'user' or 'staff'")
            continue

        user_data = {
            "username": username,
            "role": role
        }

        users.append(user_data)

        print(f"Welcome {username}! Role: {role}")
        return user_data