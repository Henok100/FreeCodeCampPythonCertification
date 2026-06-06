"""
Tower of Hanoi Solver

This module implements a recursive solution to the Tower of Hanoi puzzle.
It returns all moves required to transfer disks from the first rod to the last rod.

Rules:
- Only one disk can be moved at a time
- Only the top disk of a rod can be moved
- A larger disk cannot be placed on a smaller disk

This project was completed as part of the freeCodeCamp Python Certification.
"""


def hanoi_solver(n):
    """
    Solves the Tower of Hanoi puzzle using recursion.

    Args:
        n (int): Number of disks (must be positive integer)

    Returns:
        str: Step-by-step representation of rod states after each move
    """

    # Initialize rods:
    # A = source rod (all disks), B = helper, C = target
    A = list(range(n, 0, -1))
    B = []
    C = []

    moves = []

    def record_state():
        """
        Records the current state of all rods.
        Uses copies to avoid mutation issues during recursion.
        """
        moves.append(f"{A.copy()} {B.copy()} {C.copy()}")

    def move(disks, source, target, helper):
        """
        Recursive function to solve Tower of Hanoi.

        Args:
            disks (int): Number of disks to move
            source (list): Source rod
            target (list): Target rod
            helper (list): Helper rod
        """

        # Base case: no disks to move
        if disks == 0:
            return

        # Move n-1 disks from source to helper
        move(disks - 1, source, helper, target)

        # Move remaining disk to target
        target.append(source.pop())
        record_state()

        # Move n-1 disks from helper to target
        move(disks - 1, helper, target, source)

    # Record initial state
    record_state()

    # Solve puzzle
    move(n, A, C, B)

    return "\n".join(moves)


# Example usage (for testing only)
if __name__ == "__main__":
    print(hanoi_solver(3))