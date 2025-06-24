from add_expense import add_expense
from remove_expenses import delete_expenses
from append_expenses import append_expenses
from view_all_expenses import list_expenses
from summary import summary_expenses

# Read the contents of the JSON file
print("Welcome to expense tracker! \n What would you like to do? \n Press 1 to add an expense. \n Press 2 to delete an expense. \n Press 3 for an overview of your expenses. \n Press 4 for your total expenses. \n Press 5 to view your expenses for a certain month. \n Press 6 to append expenses. \n Press 7 to exit.")
choice = input("Enter your choice (1/2/3/4/5/6/7): ")
while choice != '7':
    if choice == '1':
        desc = input("What was the expenses for? ")
        amt = input("How much was the expenses? ") 
        add_expense(desc, amt)
    elif choice == '2':
        delete_id = input("Which expense would you like to delete? Please key in the ID: ")
        delete_expenses(delete_id)
    elif choice == '3':
        list_expenses()
    elif choice == '4':
        summary_expenses()
    elif choice == '5':
        mon = input("Please key in the month.")
        summary_expenses(mon)
    elif choice =='6':
        append_id = input("Which expense would you like to append? ")
        append_expenses(append_id)
    else:
        print("Please key in a valid choice number.")
    print("What would you like to do next? \n Press 1 to add an expense. \n Press 2 to delete an expense. \n Press 3 for an overview of your expenses. \n Press 4 for your total expenses. \n Press 5 to view your expenses for a certain month. \n Press 6 to append expenses. \n Press 7 to exit.")
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
print("Exiting expense tracker now... \n Thank you for using expenses tracker!")





