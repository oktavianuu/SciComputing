class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = sum(item["amount"] for item in self.ledger)
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = f"{item['description'][:23]}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spent.append(spent)
        total_spent += spent

    spent_percentages = [(spent / total_spent) * 100 for spent in category_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in spent_percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


# Example usage:
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
