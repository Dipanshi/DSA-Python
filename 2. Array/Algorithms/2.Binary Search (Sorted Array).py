# Binary Search (Sorted Array)
"""Find target in sorted array - O(log n)"""

def BinarySearch(arr,target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=(right+left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid -1
        
    return -1


if __name__ == "__main__":
    pos = BinarySearch([2,5,7,8,9,10,14,16],10)
    if pos==-1:
        print("Value not found!")
    else:
        print(f"Value found at pos {pos+1}")
    