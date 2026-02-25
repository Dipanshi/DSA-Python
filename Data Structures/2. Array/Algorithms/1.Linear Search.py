# Linear Search 
"""Find index of target in array - O(n)"""

def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
    
    return -1

if __name__=="__main__":
    pos = LinearSearch([1,2,5,4,8,6,9,10],0)
    if pos==-1:
        print("Value not found!")
    else:
        print(f"Value found at position {pos}")



