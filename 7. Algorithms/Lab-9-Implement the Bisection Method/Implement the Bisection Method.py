"""
Bisection Method Square Root Calculator

A Python implementation of the bisection method for approximating
the square root of a number within a specified tolerance.

This project was completed as part of the freeCodeCamp Python Certification.
"""


def square_root_bisection(number, tolerance=0.01, max_iteration=5):
    """
    Approximate the square root of a number using the bisection method.

    Args:
        number (float): Number whose square root is to be calculated.
        tolerance (float, optional): Acceptable error margin.
        max_iteration (int, optional): Maximum number of iterations.

    Returns:
        float | int | None:
            - Approximate square root if convergence succeeds.
            - The original number for inputs 0 and 1.
            - None if convergence fails.

    Raises:
        ValueError: If the number is negative.
    """

    # Square roots of negative numbers are not defined in real numbers.
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    # Handle special cases.
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    # Define initial search interval.
    low = 0
    high = 1 if number < 1 else number

    iteration = 0

    # Repeatedly halve the interval until the tolerance is met
    # or the maximum number of iterations is reached.
    while iteration < max_iteration and (high - low) > tolerance:
        mid = (low + high) / 2
        square = mid ** 2

        if square > number:
            high = mid
        else:
            low = mid

        iteration += 1

    # Check if the interval is within tolerance.
    if (high - low) <= tolerance:
        mid = (low + high) / 2
        print(
            f"The square root of {number} is approximately {mid}"
        )
        return mid

    print(f"Failed to converge within {max_iteration} iterations")
    return None