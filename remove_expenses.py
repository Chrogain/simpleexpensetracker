from filemanager import read_expenses, write_expenses

def delete_expenses(id):
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    if str(id) not in expenses:
        print(f'Expense ID {id} is not found in the tracker. Please key in another value.')
        return
   
    if str(id) in expenses:
        del expenses[id]
        print(f'Expense ID {id} deleted successfully.')


        

    