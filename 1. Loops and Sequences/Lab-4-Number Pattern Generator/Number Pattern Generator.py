"""
Number Pattern Generator

A simple Python program that generates a sequence of numbers
from 1 up to a given positive integer.

This project was completed as part of the freeCodeCamp Python Certification.
"""


def number_pattern(n):

    # Validate argument type
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Validate argument range
    if n < 1:
        return "Argument must be an integer greater than 0."

    pattern = ''

    # Build the number pattern using a loop
    for i in range(n):
        pattern += str(i + 1) + ' '

    return pattern.strip()


print(number_pattern(4))