# Repeatedly swap adjacent elements if they're in wrong order. After each pass, the largest element "bubbles up" to the end.
def bubble_sort(arr):
    """
    Bubble Sort - Simple but inefficient
    Time: O(n²) average and worst, O(n) best
    Space: O(1)
    Stable: Yes
    """
    for i in range(len(arr)):
        flag=False
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                flag=True
        if not flag:
            break
    return arr           

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original:", arr)
print("Sorted:", bubble_sort(arr.copy()))
# Output: [11, 12, 22, 25, 34, 64, 90]