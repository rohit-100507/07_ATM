account = 1000
atm_pass = 2007

transactions = []

while True:
    print("\n===== ATM MENU =====")

    print("\n1. WITHDRAW MONEY")
    print("2. CHECK BALANCE")
    print("3. ADD MONEY")
    print("4. TRANSACTION HISTORY")
    print("5. EXIT")

    choice = int(input("SELECT YOUR CHOICE : "))

    # WITHDRAW MONEY
    if choice == 1:

        attempts = 0

        while attempts < 3:

            pin = int(input("Enter Account 4 Digit Pin : "))

            if pin == atm_pass:
                amount = int(input("Enter amount to be withdrawn : "))

                if amount <= 0:
                    print("Amount must be greater than 0")

                elif amount > account:
                    print("Insufficient balance")

                else:
                    account = account - amount

                    print("===============================")
                    print(f"{amount} withdrawn successfully")
                    print(f"Remaining balance: {account}")

                    transactions.append(f"Withdraw: ₹{amount}")

                    print("===============================")

                break

            else:
                attempts += 1
                print("Invalid PIN")

                if attempts == 3:
                    print("Too many incorrect attempts.")
                    print("ATM blocked. Program exiting...")
                    print("===============================")
                    exit()

    # CHECK BALANCE
    elif choice == 2:
        print("===============================")
        print(f"Your current balance is: ₹{account}")
        print("===============================")

    # ADD MONEY
    elif choice == 3:

        attempts = 0

        while attempts < 3:

            pin = int(input("Enter Account 4 Digit Pin : "))

            if pin == atm_pass:
                amount = int(input("Enter amount to be added : "))

                if amount <= 0:
                    print("Amount must be greater than 0")

                else:
                    account = account + amount
                    
                    print("===============================")
                    print(f"{amount} added successfully")
                    print(f"Current balance: ₹{account}")

                    transactions.append(f"Deposit: ₹{amount}")
                    print("===============================")

                break

            else:
                attempts += 1
                print("Invalid PIN")

                if attempts == 3:
                    print("Too many incorrect attempts.")
                    print("ATM blocked. Program exiting...")
                    print("===============================")
                    exit()

    
    # TRANSACTION HISTORY
    elif choice == 4:

        print("\n===== TRANSACTION HISTORY =====")

        if len(transactions) == 0:
            print("No transactions yet.")

        else:
            for transaction in transactions:
                print(transaction)

        print("===============================")

    # EXIT
    elif choice == 5:
    
        print("Exited Successfully")
        break    

    else:

        print("ERROR..! Enter correct option from 1 to 5")