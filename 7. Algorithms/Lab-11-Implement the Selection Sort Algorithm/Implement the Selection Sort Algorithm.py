"""
Selection Sort Algorithm Implementation

Sorts a list in ascending order using the selection sort technique.
This algorithm repeatedly selects the smallest element from the
unsorted portion and moves it to the correct position.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def selection_sort(array):
    """
    Sorts a list in-place using selection sort.

    Args:
        array (list): List of comparable elements (e.g., integers)

    Returns:
        list: The same list, sorted in ascending order
    """

    for i in range(len(array)):
        min_index = i

        # Find the smallest element in the unsorted portion
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap only if needed (avoids unnecessary swaps)
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array