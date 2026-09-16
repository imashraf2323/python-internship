def atm():
    balance = 10000

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your current balance is: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("Updated balance: ₹", balance)
            else:
                print("Please enter a valid amount.")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount > balance:
                print("Insufficient balance!")
                print("Available balance: ₹", balance)

            elif amount <= 0:
                print("Please enter a valid amount.")

            else:
                balance -= amount
                print("Amount withdrawn successfully.")
                print("Updated balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")


atm()
