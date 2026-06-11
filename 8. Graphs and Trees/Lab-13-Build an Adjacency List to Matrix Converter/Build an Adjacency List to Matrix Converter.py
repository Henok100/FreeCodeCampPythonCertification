"""
Adjacency List to Matrix Converter

This module converts a graph represented as an adjacency list
into an adjacency matrix representation.

Each cell [i][j] in the matrix is:
- 1 if there is an edge from node i to node j
- 0 otherwise

This project demonstrates graph representation conversion.
"""


def adjacency_list_to_matrix(adj_list):
    """
    Converts an adjacency list into an adjacency matrix.

    Args:
        adj_list (dict): Dictionary where keys are nodes and values are lists of connected nodes

    Returns:
        list: 2D adjacency matrix
    """

    size = len(adj_list)
    matrix = []

    # Ensure consistent ordering of nodes
    for node in sorted(adj_list.keys()):
        row = [0] * size

        for neighbor in adj_list[node]:
            row[neighbor] = 1

        print(row)
        matrix.append(row)

    return matrix


# Example usage
if __name__ == "__main__":
    sample_graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }

    adjacency_list_to_matrix(sample_graph)