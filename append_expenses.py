from filemanager import read_expenses, write_expenses
from datetime import datetime

def overwrite_expenses(id, description, amount):
    expenses = read_expenses()
    expenses[str(id)] = {
        'date': datetime.now().isoformat(),
        'description' : description,
        'amount' : amount
    }

    write_expenses(expenses)
    print(f"Expense ID: {id} has been amemended.")


def append_expenses(id):
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return
    if id not in expenses:
        print(f'Expense {id} not found.')
        return
    else:
        del expenses[id]
        desc = input("What was the expenses for?")
        amt = input("How much was the expenses?") 
        overwrite_expenses(id, desc, amt)
        

