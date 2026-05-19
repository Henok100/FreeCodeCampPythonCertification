# Apply Discount Function

A Python function that calculates the final price of an item after applying a percentage discount, with full input validation.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Validates input types
- Ensures price is greater than 0
- Ensures discount is between 0 and 100
- Calculates final discounted price
- Returns clear error messages for invalid inputs

## Function Overview

### `apply_discount(price, discount)`

Applies a percentage discount to a given price.

#### Parameters:
- `price` (int | float): Original price
- `discount` (int | float): Discount percentage

#### Returns:
- `float`: Final price after discount
- `str`: Error message if input is invalid

## Example Usage

```python
apply_discount(50, 20)
# Output: 40.0
```

## Concepts Used

- Functions
- Type checking
- Conditional logic
- Basic arithmetic
- Input validation