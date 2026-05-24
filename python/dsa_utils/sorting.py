"""A simple collection of sorting algorithms.

Includes implementations for Quick Sort and Merge Sort.
"""

def quick_sort(arr):
    """Sorts a list using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr

    # Use the middle element as the pivot
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Sorts a list using the Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left, right):
    """Helper function to combine two sorted lists."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Grab whatever is left over
    result.extend(left[i:])
    result.extend(right[j:])

    return result
