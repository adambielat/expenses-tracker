from ast import Try
from types import ModuleType
import pandas as pd; import os; import time; import csv


# Display the money left over from budget, or over budget.
# Reminder to set income & budget on start of program
# Choices to add a weekly, monthly, yearly or one payment subscription
# Choice to set their money sign ( £, $, etc.)


expenses = []

def menu():
    os.system("cls")
    print("""
    /$$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$$  /$$     /$$
   | $$__  $$| $$  | $$| $$__  $$ /$$__  $$| $$_____/|__  $$__/| $$__  $$|  $$   /$$/
   | $$  \ $$| $$  | $$| $$  \ $$| $$  \__/| $$         | $$   | $$  \ $$ \  $$ /$$/ 
   | $$$$$$$ | $$  | $$| $$  | $$| $$ /$$$$| $$$$$      | $$   | $$$$$$$/  \  $$$$/  
   | $$__  $$| $$  | $$| $$  | $$| $$|_  $$| $$__/      | $$   | $$____/    \  $$/   
   | $$  \ $$| $$  | $$| $$  | $$| $$  \ $$| $$         | $$   | $$          | $$    
   | $$$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$$$$$$$   | $$   | $$          | $$    
   |_______/  \______/ |_______/  \______/ |________/   |__/   |__/          |__/    
                                                                                  
   1 - View total expenditure
   2 - Add an expense / purchase
   3 - Set a new budget
   4 - Set your income
                                                                                  """)
    choice = int(input("  Enter a choice: "))
    if choice not in range(1,5):
        print("  Please enter a valid choice.")
        time.sleep(2)
        menu()
    elif choice == 1:
        totalExpense()
    elif choice == 2:
        addExpense()
    elif choice == 3:
        setBudget()
    else:
        setIncome()


def addExpense():
    lst = []
    name = str(input("  What would you like to name the expense?:  "))  
    choice = str(input("""  Is this a "subscription or "payment"?:  """))
    if choice == "subscription":
        length = str(input("""  Is the subscription "weekly", "monthly" or "yearly"?:  """))
        if length == "weekly":
            cost = int(input("  How much is the payment?:  "))
            cost=cost*4.42857143
        elif length == "monthly":
            cost = int(input("  How much is the payment?:  "))
        elif length == "yearly":
            cost = int(input("  How much is the payment?:  "))
            cost=cost/12
        else:
            print("  Please enter a valid choice.")
            addExpense()
    elif choice == "payment":
        cost = int(input("  How much is the payment?:  "))
    else: 
        print("  Please enter a valid choice.")
        addExpense()
    lst.append(choice); lst.append(name), lst.append(cost)
    expenses.extend([lst])
    dataframe = pd.DataFrame(expenses, columns=["type", "name", "cost"])
    csv_file_path = 'expenses.csv'
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in dataframe.itertuples(index=False):
            writer.writerow(row)

def totalExpense():
    file_path = 'expenses.csv'
    dataframe = pd.read_csv(file_path)
    print(dataframe)

menu()

