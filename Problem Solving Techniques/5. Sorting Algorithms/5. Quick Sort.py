# Pick a pivot, partition array around pivot, recursively sort partitions.
def quick_sort(arr):
    """
    Quick Sort - Divide and Conquer
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) recursion stack
    Stable: No
    """
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left= [x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left)+mid+quick_sort(right)

# Test
arr = [10, 7, 8, 9, 1, 5]
print("Sorted:", quick_sort(arr))
# Output: [1, 5, 7, 8, 9, 10]
