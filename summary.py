from datetime import datetime
from filemanager import read_expenses

def summary_expenses(month=None):
    expenses = read_expenses()
    if not expenses:
        print("Total expenses: $0")
        return

    total_amount = 0
    if not month:
        for expense in expenses:
            total_amount += expense['amount']

        print("Total expenses: $" + str(total_amount))

    else:
        for expense in expenses:
            if datetime.fromisoformat(expense['date']).month == month:
                total_amount += expense['amount']

        print("Total expenses for " + str(month) + " : $" + str(total_amount))