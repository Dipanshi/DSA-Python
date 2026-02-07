#For each index, compute the product of all elements in the array except the element at that index.

def ProductArraySelf(arr):
    n= len(arr)
    result=[1]*n

    #left Product
    left=1
    for i in range(n):
        result[i]=left
        left *=arr[i]
    
    #right Product
    right=1
    for i in range(n-1,-1,-1):
        result[i]*=right
        right*=arr[i]
    
    return result

arr=[1, 2, 0, 4]
print(ProductArraySelf(arr))

