import json
import os

EXPENSES_FILE = 'expenses.json'

def read_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: The JSON file is corrupted.")
        user_input = input("Do you want to delete the corrupt file and continue? (yes/no): ").strip().lower()
        if user_input == 'yes':
            os.remove(EXPENSES_FILE)
            print("The corrupt file has been deleted. Returning an empty list.")
            return []
        else:
            print("Please delete the corrupt file manually to proceed.")
            exit(1)

def write_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)