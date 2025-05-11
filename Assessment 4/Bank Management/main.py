from banker import banker_menu
from customer import custer_menu
def main():
    while True:
        print("Welcome to python bank management system")
        print("Select Your Role")
        print("Press 1 --> Banker")
        print("Press 2 --> Customer")
        print("\n Press 3 --> Exit")

        ch = input("Enter Your Choice : ")

        if ch == '1':
            banker_menu()
        elif ch == '2':
            custer_menu()
        elif ch == '3':
            print("Exit Program..!")
            break
        else:
            print("Operation Invalid..!")
main()
