from filemanager import read_expenses, write_expenses
from pprint import pprint

# Read the contents of the JSON file
expenses = read_expenses()
pprint(expenses)
