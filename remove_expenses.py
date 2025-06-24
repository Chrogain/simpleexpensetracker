from filemanager import read_expenses, write_expenses

def delete_expenses(id):
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return
   
    elif str(id) in expenses:
        del expenses[str(id)]
        write_expenses(expenses)
        print(f'Expense ID {id} deleted successfully.')

    else:
        print(f'Expense ID {id} is not found in the tracker. Please key in another value.')
        return


        

    