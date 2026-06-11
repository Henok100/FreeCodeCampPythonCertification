"""
Depth-First Search (DFS) Algorithm

This module implements a depth-first search traversal on a graph
represented using an adjacency matrix.

DFS explores as far as possible along each branch before backtracking.

The output is a list of all nodes reachable from a given starting node.
"""


def dfs(adj_mat, start_node):
    """
    Performs Depth-First Search on an adjacency matrix.

    Args:
        adj_mat (list of list of int): Graph represented as adjacency matrix
        start_node (int): Starting node index

    Returns:
        list: Nodes reachable from start_node in DFS order
    """

    stack = [start_node]
    visited = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.append(current)

        # Find neighbors of current node
        neighbors = [
            index
            for index, edge in enumerate(adj_mat[current])
            if edge == 1
        ]

        for node in neighbors:
            if node not in visited and node not in stack:
                stack.append(node)

    return visited


# Example usage
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]
    ]

    print(dfs(graph, 0))