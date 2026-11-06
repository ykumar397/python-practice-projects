

class Expense:

    def __init__(self, amount, category, description):
        self.amount      = amount
        self.category    = category.lower()
        self.description = description.lower()


    def to_list(self):
        return [self.amount, self.category, self.description]
