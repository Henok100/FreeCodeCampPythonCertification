# Bisection Method Square Root Calculator

A Python implementation of the bisection method used to approximate square roots.

This project was completed as part of the freeCodeCamp Python Certification.

## Features

- Computes square roots using the bisection method
- Supports configurable tolerance
- Supports configurable iteration limits
- Handles values between 0 and 1 correctly
- Validates negative inputs
- Reports convergence failure when necessary

## How It Works

The bisection method repeatedly divides a search interval in half and selects the subinterval that contains the square root.

The process continues until:

- The interval width is smaller than the specified tolerance, or
- The maximum number of iterations is reached.

## Example Usage

```python
square_root_bisection(25)
```

### Output

```text
The square root of 25 is approximately 5.0
```

## Example: Fractional Number

```python
square_root_bisection(0.25, 0.0001, 100)
```

### Output

```text
The square root of 0.25 is approximately 0.5
```

## Concepts Used

- Numerical methods
- Binary search
- Loops
- Conditional statements
- Exception handling
- Approximation algorithms