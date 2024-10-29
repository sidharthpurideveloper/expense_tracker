import csv
import os

class BudgetManager:

    def __init__(self):
        self.budget_filename = os.path.join('data', 'budget.csv')
        self.monthly_budget = self.load_budget()

    def set_budget(self):
        try:
            self.monthly_budget = float(input("Enter your total monthly budget: "))
            self.save_budget()
            print(f"Budget set to {self.monthly_budget}.\n")
        except ValueError:
            print("Invalid input, please enter a valid number.")

    def save_budget(self):
        os.makedirs('data', exist_ok=True)
        with open(self.budget_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.monthly_budget])

    def load_budget(self):
        try:
            with open(self.budget_filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    return float(row[0])
        except (FileNotFoundError, ValueError):
            print("No saved budget found. Please set your budget.")
            return 0.0

    def track_budget(self, total_expenses):
        if total_expenses > self.monthly_budget:
            print(f"Warning: You have exceeded your budget! Total expenses: {total_expenses}, "
                  f"Budget: {self.monthly_budget}.\n")
        else:
            remaining_budget = self.monthly_budget - total_expenses
            print(f"Total expenses so far: {total_expenses}. You have {remaining_budget} left for the month.\n")
