# Hybrid of Merge Sort and Insertion Sort. Used in Python's built-in sort().
#  only awareness


def tim_sort_simplified(arr):
    """
    Simplified Tim Sort concept
    1. Divide into runs (use insertion sort on small chunks)
    2. Merge runs using merge sort
    
    Time: O(n log n)
    Space: O(n)
    Stable: Yes
    """
    MIN_MERGE = 32
    
    n = len(arr)
    
    # Sort individual runs using insertion sort
    for start in range(0, n, MIN_MERGE):
        end = min(start + MIN_MERGE, n)
        insertion_sort_range(arr, start, end)
    
    # Merge runs
    size = MIN_MERGE
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size
            end = min(start + size * 2, n)
            
            if mid < end:
                merge_runs(arr, start, mid, end)
        
        size *= 2
    
    return arr

def insertion_sort_range(arr, left, right):
    """Insertion sort for a range"""
    for i in range(left + 1, right):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_runs(arr, left, mid, right):
    """Merge two sorted runs"""
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    
    i = j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1