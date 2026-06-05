# Selection Sort Algorithm

A Python implementation of the Selection Sort algorithm.

This project was completed as part of the freeCodeCamp Python Certification.

## How It Works

Selection sort divides the list into:
- a sorted portion (left side)
- an unsorted portion (right side)

It repeatedly:
1. Finds the smallest element in the unsorted portion
2. Swaps it with the first unsorted element
3. Expands the sorted portion by one element

## Function

### `selection_sort(array)`

Sorts a list in ascending order in-place.

#### Parameters:
- `array (list)`: List of comparable elements

#### Returns:
- `list`: The sorted list

## Example

```python
print(selection_sort([5, 3, 8, 4, 2]))
```

### Output:
```text
[2, 3, 4, 5, 8]
```

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Concepts Used

- Sorting algorithms
- Nested loops
- In-place modification
- Algorithm optimization