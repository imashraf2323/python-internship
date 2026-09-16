def login():
    username = "admin"
    password = "12345"

    attempts = 0

    while attempts < 3:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Login successful!")
            break
        else:
            attempts += 1

            if attempts < 3:
                print("Incorrect username or password!")
                print("Attempts remaining:", 3 - attempts)
            else:
                print("Account locked!")


login()
