users = []

def show_menu():
    print("\n=== LOGIN SYSTEM ===")
    print("1 - Register user")
    print("2 - Login")
    print("3 - List users")
    print("4 - Exit")
    print("5 - Close account")

while True:

    show_menu()

    option = input("Choose an option: ")

    if option == "1":

        name = input("Enter username: ")
        password = input("Enter password: ")

        if name in [u["name"] for u in users]:

            print("User already exists. Try another username.")

        else:

            user = {
                "name": name,
                "password": password,
                "status": "active"
            }

            users.append(user)

            print("User registered successfully!")

    elif option == "2":

        login_name = input("Enter your username: ")
        login_password = input("Enter your password: ")

        login_success = False

        for user in users:

            if user["name"] == login_name and user["password"] == login_password:

                if user["status"] == "closed":

                    print("Account closed. Contact support for more information.")

                else:

                    print("Welcome! We are very happy to have you here!")

                login_success = True

        if login_success == False:

            print("Incorrect username or password.")

    elif option == "3":

        print("\n=== REGISTERED USERS ===")

        if len(users) == 0:

            print("No registered users.")

        else:

            for user in users:

                print(f"Name: {user['name']}")
                print(f"Status: {user['status']}")
                print("----------------------")

    elif option == "4":

        print("Exiting system...")
        break

    elif option == "5":

        close_name = input("Enter your username to close the account: ")
        close_password = input("Enter your password: ")

        for user in users:

            if user["name"] == close_name and user["password"] == close_password:

                user["status"] = "closed"

                print("Account closed successfully!")

                break

        else:

            print("Incorrect username or password.")

    else:

        print("Invalid option. Try again.")