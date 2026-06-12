"""
N-Queens Problem Solver using Depth-First Search (Backtracking)

The N-Queens problem places N queens on an N×N chessboard
so that no two queens attack each other.

Rules:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

Each solution is represented as a list where:
index = row number
value = column position of the queen
"""


def dfs_n_queens(n):
    """
    Solves the N-Queens problem using DFS backtracking.

    Args:
        n (int): Size of the chessboard (n x n)

    Returns:
        list: A list of all valid solutions.
              Each solution is a list of column positions.
    """

    if n < 1:
        return []

    used_cols = set()
    used_diag1 = set()  # r - c
    used_diag2 = set()  # r + c

    solutions = []
    current = []

    def backtrack(row):
        # Base case: all queens placed
        if row == n:
            solutions.append(current.copy())
            return

        for col in range(n):

            if (
                col in used_cols or
                (row - col) in used_diag1 or
                (row + col) in used_diag2
            ):
                continue

            # choose
            current.append(col)
            used_cols.add(col)
            used_diag1.add(row - col)
            used_diag2.add(row + col)

            # explore
            backtrack(row + 1)

            # un-choose (backtrack)
            current.pop()
            used_cols.remove(col)
            used_diag1.remove(row - col)
            used_diag2.remove(row + col)

    backtrack(0)

    return solutions


# Example usage
if __name__ == "__main__":
    print(dfs_n_queens(4))