"""
Budget App

A simple budgeting system that tracks deposits, withdrawals,
transfers, and visual spending distribution across categories.

This project was completed as part of the freeCodeCamp Python Certification.
"""


class Category:
    """
    Represents a budget category that tracks financial transactions.
    """

    def __init__(self, name):
        """
        Initialize a budget category.

        Args:
            name (str): Name of the budget category.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Record a deposit transaction.

        Args:
            amount (float): Amount to deposit.
            description (str): Optional description of the transaction.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Record a withdrawal transaction if sufficient funds exist.

        Args:
            amount (float): Amount to withdraw.
            description (str): Optional description.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description}
            )
            return True
        return False

    def get_balance(self):
        """
        Calculate current balance of the category.

        Returns:
            float: Total balance.
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfer funds to another category.

        Args:
            amount (float): Amount to transfer.
            category (Category): Destination category.

        Returns:
            bool: True if transfer succeeded, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(
                amount,
                description=f"Transfer to {category.name}"
            )
            category.deposit(
                amount,
                description=f"Transfer from {self.name}"
            )
            return True
        return False

    def check_funds(self, amount):
        """
        Check if enough funds are available.

        Args:
            amount (float): Amount to check.

        Returns:
            bool: True if sufficient funds exist, False otherwise.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Return formatted string representation of category ledger.

        Returns:
            str: Formatted budget report.
        """
        output = f"{self.name:*^30}\n"

        for item in self.ledger:
            output += (
                f"{item['description'][:23]:<23}"
                f"{item['amount']:>7.2f}\n"
            )

        output += f"Total: {self.get_balance()}"

        return output


def create_spend_chart(categories):
    """
    Create a bar chart showing percentage spent per category.

    Args:
        categories (list): List of Category objects.

    Returns:
        str: Formatted spending chart.
    """

    output = "Percentage spent by category\n"

    total_spent = 0
    totals = []

    # Calculate total spending per category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
                total_spent += abs(item["amount"])
        totals.append(spent)

    # Convert to percentages (rounded down to nearest 10)
    percentages = [
        (int((amount / total_spent) * 100) // 10) * 10
        for amount in totals
    ]

    # Build bar chart
    for level in range(100, -1, -10):
        output += f"{level:>3}| "

        for p in percentages:
            output += "o  " if p >= level else "   "

        output += "\n"

    # Horizontal line
    output += "    -" + "---" * len(categories) + "\n"

    # Vertical category names
    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        line = "     "

        for name in names:
            line += (name[i] + "  ") if i < len(name) else "   "

        output += line + "\n"

    return output.rstrip("\n")