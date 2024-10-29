class Expense:

    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def is_valid(self):
        return all([self.date, self.category, self.amount, self.description])

    def display(self):
        print(f"Date: {self.date}, Category: {self.category}, Amount: {self.amount}, Description: {self.description}")
