
import json

# File to save the expenses
data_file = "expenses.json"

# Load existing data if the file exists
def load_expenses():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter a description (optional): ")
    
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\nRecorded Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
    print()

# View total expenses by category
def view_total_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\nTotal Expenses by Category:")
    for category, total in totals.items():
        print(f"{category}: {total}")
    print()

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()