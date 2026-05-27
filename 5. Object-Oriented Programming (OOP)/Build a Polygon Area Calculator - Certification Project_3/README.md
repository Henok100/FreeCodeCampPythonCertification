# Polygon Area Calculator

An object-oriented Python project that models rectangles and squares and performs geometric calculations.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Rectangle and Square classes
- Area, perimeter, and diagonal calculations
- Shape visualization using ASCII art
- Shape fitting calculations
- Proper inheritance and polymorphism

## Classes

### Rectangle

Represents a rectangle with width and height.

#### Methods:
- `set_width()`
- `set_height()`
- `get_area()`
- `get_perimeter()`
- `get_diagonal()`
- `get_picture()`
- `get_amount_inside()`

### Square

Inherits from Rectangle and enforces equal sides.

#### Methods:
- `set_side()`
- overrides `set_width()` and `set_height()`

## Example Usage

```python
rect = Rectangle(4, 8)
print(rect.get_area())
print(rect.get_picture())

sq = Square(5)
print(sq)
```

## Example Output

```text
Rectangle(width=4, height=8)
****
****
****
****
****
****
****
****
```

## Concepts Used

- Object-Oriented Programming
- Inheritance
- Method overriding
- Geometry calculations
- String manipulation
- Class design principles