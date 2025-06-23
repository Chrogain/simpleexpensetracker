from filemanager import read_expenses
from datetime import datetime

def list_expenses():
    expenses = read_expenses()
    if not expenses:
        print("There are no expenses.")

    else:    
        print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<10}")

        for expense_id, expense in expenses.items():
            print(f"{expense_id:<4} {datetime.fromisoformat(expense['date']).strftime('%d-%B-%Y'):<12} "
                  f"{expense['description']:<15} {expense['amount']:<10.2f}")



