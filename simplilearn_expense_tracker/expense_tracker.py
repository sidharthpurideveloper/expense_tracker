import csv
import os
from expense import Expense

class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.expense_filename = os.path.join('data', 'expenses.csv')
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            for expense in self.expenses:
                if expense.is_valid():
                    expense.display()
                else:
                    print("Incomplete expense entry found, skipping...")

    def save_expenses(self):
        os.makedirs('data', exist_ok=True)
        with open(self.expense_filename, mode='w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for expense in self.expenses:
                writer.writerow({
                    'date': expense.date,
                    'category': expense.category,
                    'amount': expense.amount,
                    'description': expense.description
                })

    def load_expenses(self):
        try:
            with open(self.expense_filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append(Expense(
                        row['date'],
                        row['category'],
                        float(row['amount']),
                        row['description']
                    ))
        except FileNotFoundError:
            print("No saved expense file found, starting with an empty expense list.")

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
