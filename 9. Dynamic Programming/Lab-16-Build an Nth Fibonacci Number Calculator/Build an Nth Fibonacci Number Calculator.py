"""
Nth Fibonacci Number Calculator

This module computes the nth Fibonacci number using a dynamic programming approach.

The Fibonacci sequence is defined as:
0, 1, 1, 2, 3, 5, 8, ...

Each number is the sum of the two preceding numbers.

This implementation builds the sequence iteratively for efficiency.
"""


def fibonacci(n):
    """
    Computes the nth Fibonacci number using dynamic programming.

    Args:
        n (int): A non-negative integer representing the position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """

    # Base cases: first two Fibonacci numbers
    if n == 0 or n == 1:
        return n

    # Initialize sequence with first two Fibonacci numbers
    sequence = [0, 1]

    # Build sequence up to n
    while len(sequence) <= n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence[n]


# Example usage
if __name__ == "__main__":
    print(fibonacci(10))