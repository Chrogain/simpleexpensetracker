from filemanager import read_expenses

def list_expenses():
    expenses = read_expenses()
    if not expenses:
        print("There are no expenses.")

        print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Amount':<10}")

        for expense in expenses:
            print(f"{expense['id']:<4} {expense['date']:<12} "
                  f"{expense['description']:<15} {expense['amount']:<10}")



