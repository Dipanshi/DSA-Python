# Find the minimum element and place it at the beginning. Repeat for remaining unsorted portion.
def selection_sort(arr):
    """
    Selection Sort
    Time: O(n²) all cases
    Space: O(1)
    Stable: No
    """
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

    return arr

# Test
arr = [64, 25, 12, 22, 11]
print("Unsorted Array:", arr)
print("Sorted:", selection_sort(arr))
# Output: [11, 12, 22, 25, 64]