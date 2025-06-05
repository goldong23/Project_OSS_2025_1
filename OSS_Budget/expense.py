
class Expense:
    def __init__(self, date, category, description, amount, reason):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.reason = reason

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"