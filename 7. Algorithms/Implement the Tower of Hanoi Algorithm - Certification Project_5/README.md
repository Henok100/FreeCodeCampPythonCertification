# Tower of Hanoi Solver

A simple recursive Python solution for the classic Tower of Hanoi puzzle.

This project was completed as part of the freeCodeCamp Python Certification.

---

## 📌 Problem

Move `n` disks from the first rod to the last rod using:

- Only one disk at a time
- Only the top disk can be moved
- No larger disk can be placed on a smaller disk

---

## ⚙️ Function

### `hanoi_solver(n)`

Solves the Tower of Hanoi puzzle and returns each step.

#### Parameters:
- `n (int)`: Number of disks

#### Returns:
- `str`: Each move printed line by line showing rod states

---

## 🧪 Example

```python
print(hanoi_solver(3))
```

---

## 📤 Example Output

```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
...
[] [] [3, 2, 1]
```

---

## 🧠 Concept Used

- Recursion
- Problem decomposition
- Stack-like movement logic
- State tracking

---

## 🚀 Learning Outcome

This project helps understand:
- how recursion breaks problems into smaller steps
- how the call stack works
- how complex problems can be solved with simple rules