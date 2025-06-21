from filemanager import read_expenses, write_expenses
from datetime import datetime

def add_expense(description, amount):
    if amount <= 0:
        print("Invalid amount. Please enter the amount again.")
        return
    try:
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount. Please enter the amount again.")
            return
        if round(amount, 2) != amount:
            raise ValueError("Please only enter an amount up to 2 decimal places.")
    except ValueError as e:
        print(f"{e}")
        return
    
    expenses = read_expenses()

    if not expenses:
        id = 1
    else:
        id = max(map(int, expenses.keys())) + 1

    expenses[str(id)] = {
        'date': datetime.now().isoformat(),
        'description' : description,
        'amount' : amount
    }

    write_expenses(expenses)
    print(f"Expense ID: {id} added.")
    

            
        