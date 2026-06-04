"""
Quicksort Algorithm Implementation

Sorts a list of integers using the divide-and-conquer quicksort method.
"""


def quick_sort(array):
    """
    Sorts a list using the quicksort algorithm.

    Args:
        array (list): List of integers.

    Returns:
        list: Sorted list in ascending order.
    """

    # Base case: empty or single-element list is already sorted
    if len(array) <= 1:
        return array

    # Choose pivot (first element)
    pivot = array[0]

    # Partition into three sublists
    less_array = [x for x in array if x < pivot]
    equal_array = [x for x in array if x == pivot]
    greater_array = [x for x in array if x > pivot]

    # Recursive sorting + concatenation
    return quick_sort(less_array) + equal_array + quick_sort(greater_array)