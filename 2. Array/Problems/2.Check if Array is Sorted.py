# Check if Array is sorted or not

def CheckArraySorted(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True

arr = [1,2,3,5,8,9,10]
arr2=[2,6,1,6,4,7,9]

print(CheckArraySorted(arr))
print(CheckArraySorted(arr2))