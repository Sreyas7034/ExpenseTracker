import sqlite3
from database import setup_database  # Importing setup_database from database.py

def add_expense(date, category, amount, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)''', (date, category, amount, description))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_expense(expense_id, date, category, amount, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?''', (date, category, amount, description, expense_id))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            while True:
                try:
                    amount = float(input("Enter amount: "))  # Convert input directly to float
                    break  # Break the loop if conversion is successful
                except ValueError:
                    print("Invalid input for amount. Please enter a numeric value.")
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")
        
        elif choice == '2':
            expenses = view_expenses()
            for expense in expenses:
                print(expense)
        
        elif choice == '3':
            expense_id = int(input("Enter the ID of the expense to update: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            category = input("Enter new category: ")
            while True:
                try:
                    amount = float(input("Enter new amount: "))
                    break
                except ValueError:
                    print("Invalid input for amount. Please enter a numeric value.")
            description = input("Enter new description: ")
            update_expense(expense_id, date, category, amount, description)
            print("Expense updated successfully!")
        
        elif choice == '4':
            expense_id = int(input("Enter the ID of the expense to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully!")
        
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    setup_database()
    main()
