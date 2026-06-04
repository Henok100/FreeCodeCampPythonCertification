# Quicksort Algorithm Implementation

A Python implementation of the Quicksort algorithm using recursion and list partitioning.

This project was completed as part of the freeCodeCamp Python Certification.

## How It Works

Quicksort is a divide-and-conquer algorithm:

1. Choose a pivot element
2. Partition the list into:
   - elements less than the pivot
   - elements equal to the pivot
   - elements greater than the pivot
3. Recursively sort the sublists
4. Combine the results

## Function

### `quick_sort(array)`

Sorts a list of integers in ascending order.

#### Parameters:
- `array (list)`: List of integers

#### Returns:
- `list`: Sorted list

## Example Usage

```python
print(quick_sort([5, 3, 8, 4, 2]))
```

### Output:
```text
[2, 3, 4, 5, 8]
```

## Concepts Used

- Recursion
- Divide and conquer
- List comprehensions
- Sorting algorithms
- Algorithm design