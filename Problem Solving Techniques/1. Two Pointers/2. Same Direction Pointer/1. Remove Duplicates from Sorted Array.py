    # Remove duplicates in-place, return new length
    # Time: O(n), Space: O(1)
def RemoveDuplicate(arr):
    if not arr:
        return 0
    slow=0
    for fast in range(len(arr)):
        if arr[fast]!=arr[slow]:
            arr[slow+1],arr[fast]=arr[fast],arr[slow+1]
            slow+=1
        
    return arr[:slow+1]
    
print(RemoveDuplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))