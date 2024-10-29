from expense_tracker import ExpenseTracker
from budget_manager import BudgetManager
from expense import Expense

class ExpenseManagerApp:

    def __init__(self):
        self.tracker = ExpenseTracker()
        self.budget_manager = BudgetManager()

    def add_expense(self):
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Travel, etc.): ")
        try:
            amount = float(input("Enter the amount spent: "))
        except ValueError:
            print("Invalid amount, please enter a valid number.")
            return
        description = input("Enter a brief description of the expense: ")

        total_expenses = self.tracker.get_total_expenses() + amount
        if total_expenses > self.budget_manager.monthly_budget:
            print(f"Error: Adding this expense exceeds your budget of {self.budget_manager.monthly_budget}.")
        else:
            expense = Expense(date, category, amount, description)
            self.tracker.add_expense(expense)

    def display_menu(self):
        while True:
            try:
                print("\nExpense Tracker Menu:")
                print("1. Add expense")
                print("2. View expenses")
                print("3. Set and Track budget")
                print("4. Save expenses")
                print("5. Exit")

                choice = input("Choose an option: ")

                if choice == '1':
                    self.add_expense()
                elif choice == '2':
                    self.tracker.view_expenses()
                elif choice == '3':
                    if self.budget_manager.monthly_budget == 0:
                        self.budget_manager.set_budget()
                    total_expenses = self.tracker.get_total_expenses()
                    self.budget_manager.track_budget(total_expenses)
                elif choice == '4':
                    self.tracker.save_expenses()
                elif choice == '5':
                    self.tracker.save_expenses()
                    print("Exiting the program...")
                    break
                else:
                    print("Invalid option. Please choose again.")
            except KeyboardInterrupt:
                print("\nRestarting the menu...")
                return

if __name__ == '__main__':
    app = ExpenseManagerApp()
    app.display_menu()
