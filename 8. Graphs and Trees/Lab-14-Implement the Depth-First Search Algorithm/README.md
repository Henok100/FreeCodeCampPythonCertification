# Depth-First Search (DFS) Algorithm

This project implements the Depth-First Search (DFS) algorithm using an adjacency matrix representation of a graph.

DFS is a graph traversal technique that explores as far as possible along a branch before backtracking.

---

## 📌 How it works

- Start from a given node
- Visit a neighbor node
- Continue going deeper until no more unvisited nodes exist
- Backtrack and explore remaining branches

---

## ⚙️ Function

### `dfs(adj_mat, start_node)`

Performs DFS traversal on a graph.

### Parameters:
- `adj_mat (list of list of int)`: adjacency matrix
- `start_node (int)`: starting node index

### Returns:
- `list`: nodes visited in DFS order

---

## 🧪 Example

```python
graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]

print(dfs(graph, 0))
```

---

## 📤 Output

```
[0, 2, 3, 1]
```

---

## 🧠 Concepts Used

- Graph traversal
- Stack (LIFO)
- Adjacency matrix representation
- Depth-first search strategy

---

## 🚀 Learning Outcome

This project helps you understand:
- how DFS explores graphs
- how stacks control traversal order
- how graph structures are processed algorithmically