# Reverse an Array

# Method 1: Using slicing - O(n) space
def reverseArray1(arr):
    return arr[::-1]

#Method 2: In-place using two pointers - O(1) space
def reverseArrayInplace(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

# Method 3: Using built-in
#arr.reverse()

if __name__=="__main__":
    arr=[10,3,50,2,60,2,40]
    arr.reverse()
    print(reverseArray1([1,3,5,2,6,2,4]))
    print(reverseArrayInplace([10,30,50,20,60,20,40]))
    print(arr)
