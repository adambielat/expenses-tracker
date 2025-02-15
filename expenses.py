from ast import Try
from types import ModuleType
import pandas as pd; import os; import time; import csv


# Display the money left over from budget, or over budget.
# Reminder to set income & budget on start of program
# Choices to add a weekly, monthly, yearly or one payment subscription
# Choice to set their money sign ( £, $, etc.)


expenses = []; theBudget = []

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
    file_path = 'expenses.csv'
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in dataframe.itertuples(index=False):
            writer.writerow(row)

def totalExpense():
    os.system("cls")
    cost_file_path = 'expenses.csv'
    budget_file_path = 'budget.csv'
    dataframe = pd.read_csv(cost_file_path)
    dataframe2 = pd.read_csv(budget_file_path)
    print()
    print(dataframe)
    total = dataframe['cost'].sum()
    endbudget = dataframe2['budget'].head(1).sum()
    print()
    print(f"""  Total spent: £{total}
  
  Budget: £{endbudget}
  Money left: £{endbudget - total}
  """)
    choice = input("  Press enter to return to the menu.")
    if choice == "":
        menu()


def setBudget():
    os.system("cls")
    print()
    try:
        budget_ = int(input("  What is your new budget?:  "))
        if budget_ < 0:
            print("  Please enter a valid budget.")
            setBudget()
    except ValueError:
        print("  Please enter a valid budget.")
        setBudget()
    theBudget.extend(["budget", budget_])
    file_path = 'budget.csv'
    dataframe2 = pd.DataFrame(theBudget, columns=['budget'])
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in dataframe2.itertuples(index=False):
            writer.writerow(row)
    print(f"  Successfully set budget to £{budget_}")
    print()
    choice = input("  Press enter to return to the menu.")
    if choice == "":
        menu()


menu()

