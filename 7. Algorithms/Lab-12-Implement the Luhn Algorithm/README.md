# Luhn Algorithm Validator

A Python implementation of the Luhn algorithm used to validate identification numbers such as credit card numbers.

This project was completed as part of the freeCodeCamp Python Certification.

## How It Works

The Luhn algorithm:
1. Removes spaces and dashes from the input
2. Reverses the digits
3. Doubles every second digit
4. Subtracts 9 if a doubled digit is greater than 9
5. Sums all digits
6. Checks if the total is divisible by 10

## Function

### `verify_card_number(card_number)`

Validates a card number string.

#### Parameters:
- `card_number (str)`: The card number (may contain spaces or dashes)

#### Returns:
- `"VALID!"` if the number is valid
- `"INVALID!"` otherwise

## Example

```python
print(verify_card_number("4111-1111-1111-1111"))
```

### Output:
```text
VALID!
```

## Concepts Used

- String manipulation
- Loops
- Conditional logic
- Algorithm implementation
- Data validation