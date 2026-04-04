# main.py

from auth import login
from post import create_post, view_posts, update_post, delete_post, search_posts


def main():
    while True:

        print("\n=== MAIN MENU ===")
        print("1. Login")
        print("2. Exit")

        start_choice = input("Choose option: ")

        if start_choice == "1":
            user = login()

            if user is None:
                continue

            while True:
                print("\n--- MENU ---")

                # USER MENU
                if user["role"] == "user":
                    print("1. Create Post")
                    print("2. View Posts")
                    print("3. Update Post")
                    print("4. Delete Post")
                    print("5. Logout")

                    choice = input("Choose option: ")

                    if choice == "1":
                        create_post(user)
                    elif choice == "2":
                        view_posts()
                    elif choice == "3":
                        update_post(user)
                    elif choice == "4":
                        delete_post(user)
                    elif choice == "5":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice!")

                # STAFF MENU
                elif user["role"] == "staff":
                    print("1. View Posts")
                    print("2. Search Posts")
                    print("3. Logout")

                    choice = input("Choose option: ")

                    if choice == "1":
                        view_posts()
                    elif choice == "2":
                        search_posts()
                    elif choice == "3":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice!")

        elif start_choice == "2":
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()