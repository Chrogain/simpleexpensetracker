from filemanager import read_expenses, write_expenses
from add_expense import add_expense
from summary import summary_expenses
from view_all_expenses import list_expenses
from pprint import pprint

# Read the contents of the JSON file
print("Welcome to expense tracker! \n What would you like to do? \n Press 1 to add an expense. \n Press 2 to delete an expense. \n Press 3 for an overview of your expenses. \n Press 4 for your total expenses. \n Press 5 to view your expenses for a certain month. \n Press 6 to exit.")
choice = input("Enter your choice (1/2/3/4/5/6): ")
while choice != '6':
    if choice == '1':
        desc = input("What was the expenses for?")
        amt = input("How much was the expenses?") 
        add_expense(desc, amt)
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
print("Exiting expense tracker now... \n Thank you for using expenses tracker!")


