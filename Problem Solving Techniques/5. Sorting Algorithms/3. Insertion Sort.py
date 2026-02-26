# Build sorted array one element at a time by inserting each element into its correct position.
def insertion_sort(arr):
    """
    Insertion Sort
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    Stable: Yes
    """
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key            
    return arr

# Test
arr = [12, 11, 13, 5, 6]
print("Sorted:", insertion_sort(arr.copy()))
# Output: [5, 6, 11, 12, 13]