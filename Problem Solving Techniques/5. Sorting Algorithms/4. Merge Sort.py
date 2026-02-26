# Divide array into halves, recursively sort them, and merge sorted halves.
def merge_sort(arr):
    """
    Merge Sort - Divide and Conquer
    Time: O(n log n) all cases
    Space: O(n)
    Stable
    """
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    sort_arr=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            sort_arr.append(left[l])
            l+=1
        else:
            sort_arr.append(right[r])
            r+=1

    sort_arr.extend(left[l:])
    sort_arr.extend(right[r:])

    return sort_arr

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted:", merge_sort(arr))
# Output: [3, 9, 10, 27, 38, 43, 82]