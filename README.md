# ATM Management System - Python

This is one of my beginner Python projects.

I created this **ATM Management System** to practice Python concepts such as **while loops, conditional statements, lists, functions of lists, user input, validation, and basic program logic**.

The program provides a simple ATM menu where the user can withdraw money, check their balance, add money, view transaction history, or exit the program.

## Features

* Withdraw money
* Check account balance
* Add money to the account
* View transaction history
* PIN verification
* Maximum 3 incorrect PIN attempts
* ATM blocks and exits after 3 incorrect PIN attempts
* Checks for insufficient balance
* Prevents entering zero or negative amounts
* Handles invalid menu choices

## Python Concepts Used

* Variables
* Integer data type
* `input()`
* `if`, `elif`, and `else`
* `while` loop
* `for` loop
* Lists
* `append()`
* `len()`
* `break`
* `exit()`
* f-strings
* Basic validation
* Menu-driven programming

## How It Works

When the program starts, the account has an initial balance of **₹1000**.

The user is shown the following menu:

```text
===== ATM MENU =====

1. WITHDRAW MONEY
2. CHECK BALANCE
3. ADD MONEY
4. TRANSACTION HISTORY
5. EXIT
```

For withdrawal and deposit operations, the user must enter the correct 4-digit PIN.

If the PIN is entered incorrectly, the user gets a maximum of **3 attempts**. After 3 incorrect attempts, the program exits.

## Example Output

```text
===== ATM MENU =====

1. WITHDRAW MONEY
2. CHECK BALANCE
3. ADD MONEY
4. TRANSACTION HISTORY
5. EXIT

SELECT YOUR CHOICE : 1
Enter Account 4 Digit Pin : 2007
Enter amount to be withdrawn : 300

===============================
300 withdrawn successfully
Remaining balance: 700
===============================
```

Checking the balance:

```text
===== ATM MENU =====

1. WITHDRAW MONEY
2. CHECK BALANCE
3. ADD MONEY
4. TRANSACTION HISTORY
5. EXIT

SELECT YOUR CHOICE : 2

===============================
Your current balance is: ₹700
===============================
```

Adding money:

```text
SELECT YOUR CHOICE : 3
Enter Account 4 Digit Pin : 2007
Enter amount to be added : 500

===============================
500 added successfully
Current balance: ₹1200
===============================
```

Transaction history:

```text
===== TRANSACTION HISTORY =====
Withdraw: ₹300
Deposit: ₹500
===============================
```

## What I Learned

Through this project, I practiced how to build a **menu-driven program** and how to use loops and conditions to control different operations.

I also learned how to store transaction information in a **list** and use `append()` to add new transactions.

This project helped me improve my understanding of **program logic, validation, loops, and user interaction in Python**.

## Future Improvements

In the future, I can improve this project by adding:

* Multiple bank accounts
* Account number
* Separate PIN for each account
* Transfer money
* Change PIN option
* Transaction date and time
* Receipt generation
* Saving transactions to a file

## Author

Beginner Python project created for learning and practicing Python programming.
