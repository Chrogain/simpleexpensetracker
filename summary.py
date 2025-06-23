from datetime import datetime
from filemanager import read_expenses

def summary_expenses(month=None):
    expenses = read_expenses()
    if not expenses:
        print("Total expenses: $0")
        return

    total_amount = 0
    if not month:
        for expense in expenses.values():
            total_amount += expense['amount']

        print(f"Total expenses: ${total_amount:.2f}")

    else:
        try:
            month_num = datetime.strptime(month, "%B").month
            for expense in expenses.values():
             if datetime.fromisoformat(expense['date']).month == month_num:
                    total_amount += expense['amount']

            print(f"Total expenses for {month}: ${total_amount:.2f}")
        
        except ValueError as e:
            print("Please provide the full name of the month.")