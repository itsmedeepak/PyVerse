"""
Mini Expense Tracker
A simple Python program to track your daily expenses.
You can add expenses, view all expenses, and get the total amount spent.
Suitable for beginner contributors to PyVerse.
"""

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    expenses.append({"name": name, "amount": amount})
    print(f"Added: {name} - ${amount:.2f}")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']} - ${expense['amount']:.2f}")
    print(f"Total Spent: ${sum(e['amount'] for e in expenses):.2f}\n")

def main():
    while True:
        print("\n--- Mini Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
