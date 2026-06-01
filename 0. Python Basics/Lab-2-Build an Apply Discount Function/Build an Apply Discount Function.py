"""
Apply Discount Function

Calculates the final price of an item after applying a percentage discount.
Includes input validation to ensure correct data types and valid ranges.
"""


def apply_discount(price, discount):
    # Validate price type
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # Validate discount type
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # Validate price value
    if price <= 0:
        return "The price should be greater than 0"

    # Validate discount range
    if not (0 <= discount <= 100):
        return "The discount should be between 0 and 100"

    # Calculate final price after discount
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price