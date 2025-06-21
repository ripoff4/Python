import os
from datetime import datetime
import time


def add_transaction(balance, income, expense):
    while True:
        category = input("➕ Income or ➖ Expense : ")
        amount = int(input("💵 Amount : "))
        reason = input("📝 Enter the reason of transcation : ")
        if category.startswith('i'):
            balance += amount
            income += amount
            current_date = datetime.now().strftime("%d-%m-%Y")
            str = f"\n{current_date}|+{amount}|{reason}|{income}|{expense}|{balance}"
            data = str.encode()
            fd = os.open('transactions.txt', os.O_WRONLY |
                         os.O_APPEND | os.O_CREAT)
            os.write(fd, data)
            print("☑️ Transaction added succesfully")
            break
        elif category.startswith('e'):
            if balance < amount:
                print("❌ You can't proceed beacause of low balance")
            else:
                balance -= amount
                expense += amount
                current_date = datetime.now().strftime("%d-%m-%Y")
                str = f"\n{current_date}|-{amount}|{reason}|{income}|{expense}|{balance}"
                data = str.encode()
                fd = os.open('transactions.txt', os.O_WRONLY |
                             os.O_APPEND | os.O_CREAT)
                os.write(fd, data)
                print("☑️ Transaction added succesfully")
                break
        else:
            print("Enter valid category of transaction")


def view_summary(balance, income, expense):
    print("📊 Financial Summary 📊")
    print(f"💰 Income : +{income}")
    print(f"💸 Expense : -{expense}")
    print(f"💲 Balance : {balance}")


def transaction():
    while True:
        print("====Financial Tracker====")
        file_path = "transactions.txt"
        balance, income, expense = 0, 0, 0
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    documents = last_line.split("|")
                    balance += int(documents[-1])
                    expense += int(documents[-2])
                    income += int(documents[-3])
        print("Choose an option: ")
        print("1. 💵 Add Transaction")
        print("2. 💲 View Transaction")
        print("3. 📊 View Summary")
        print("4. 🚪 Exit")
        choice = int(input("Choose an option (1-4) : "))
        if choice == 1:
            add_transaction(balance, income, expense)
        elif choice == 2:
            with open('transactions.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

        elif choice == 3:
            view_summary(balance, income, expense)
        elif choice == 4:
            os.system("cls")
            break
        time.sleep(5)
        os.system("cls")


transaction()
