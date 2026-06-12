# N-Queens Solver (DFS Backtracking)

This project solves the classic N-Queens problem using depth-first search (backtracking).

The goal is to place N queens on an N×N chessboard so that no two queens attack each other.

---

## 📌 Problem Rules

A valid solution ensures:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

---

## ⚙️ Function

### `dfs_n_queens(n)`

Finds all valid board configurations.

### Parameters:
- `n (int)`: size of the chessboard

### Returns:
- `list`: all valid solutions

Each solution is represented as:

```
[row 0 col, row 1 col, row 2 col, ...]
```

---

## 🧪 Example

```python
print(dfs_n_queens(4))
```

---

## 📤 Example Output

```
[[1, 3, 0, 2], [2, 0, 3, 1]]
```

---

## 🧠 Concepts Used

- Backtracking
- Depth-first search (DFS)
- Constraint satisfaction
- Recursion
- Set optimization

---

## 🚀 Learning Outcome

This project helps you understand:
- how recursive backtracking explores solution spaces
- how constraints prune invalid paths
- how DFS is used in combinatorial problems