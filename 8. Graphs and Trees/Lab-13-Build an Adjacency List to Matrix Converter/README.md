# Adjacency List to Matrix Converter

A simple Python function that converts a graph from an adjacency list representation into an adjacency matrix.

This project demonstrates basic graph theory and data structure conversion.

---

## 📌 Problem

Given an adjacency list:

```python
{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
```

Convert it into an adjacency matrix:

```
[0, 1, 1, 0]
[0, 0, 1, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]
```

---

## ⚙️ Function

### `adjacency_list_to_matrix(adj_list)`

Converts adjacency list into adjacency matrix.

### Parameters:
- `adj_list (dict)`: Graph representation

### Returns:
- `list`: 2D adjacency matrix

---

## 🧪 Example

```python
adjacency_list_to_matrix({
    0: [2],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2]
})
```

---

## 🧠 Concepts Used

- Graph representation
- Adjacency lists
- Adjacency matrices
- Nested loops
- Data structure conversion

---

## 🚀 Learning Outcome

This project helps you understand:
- how graphs are represented in different formats
- how to convert between representations
- basic algorithmic thinking in graph theory