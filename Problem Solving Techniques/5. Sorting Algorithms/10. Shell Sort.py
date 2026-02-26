# Generalization of insertion sort that allows exchange of far items.

def shell_sort(arr):
    """
    Shell Sort - Improved Insertion Sort
    Time: O(n log n) to O(n²) depending on gap sequence
    Space: O(1)
    Stable: No
    """
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        # Perform gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Shift elements until correct position
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    return arr

# Test
arr = [12, 34, 54, 2, 3]
print("Sorted:", shell_sort(arr.copy()))
# Output: [2, 3, 12, 34, 54]