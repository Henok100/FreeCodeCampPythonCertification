"""
Luhn Algorithm Implementation

This module validates identification numbers (such as credit card numbers)
using the Luhn checksum algorithm.
"""

def verify_card_number(card_number):
    """
    Validates a card number using the Luhn algorithm.

    The function:
    - Removes spaces and dashes
    - Applies Luhn checksum logic
    - Returns VALID! or INVALID!

    Args:
        card_number (str): Card number string possibly containing spaces or dashes

    Returns:
        str: "VALID!" if the number is valid, otherwise "INVALID!"
    """

    # Remove spaces and hyphens
    card_number = card_number.replace('-', '').replace(' ', '')

    # Convert to digits
    digits = [int(d) for d in card_number]

    # Reverse digits for Luhn processing
    digits.reverse()

    total = 0

    for i in range(len(digits)):
        num = digits[i]

        # Double every second digit
        if i % 2 == 1:
            num *= 2

            # If result is two-digit, subtract 9
            if num > 9:
                num -= 9

        total += num

    # Valid if total is divisible by 10
    return "VALID!" if total % 10 == 0 else "INVALID!"