# Remove Duplicates (Sorted Array)

#Method 1 time complexity O(N) and space Complexity O(N)
def RemoveDuplicate_method1(arr):
    if arr is None:
        return arr
    res=[]
    for i in arr:
        if i not in res:
            res.append(i)
    
    return res

#Method 2 time complexity O(N) and space Complexity O(1)
def RemoveDuplicate_method2(arr):
    if arr is None:
        return 0
    write_index=1
    for i in range(1,len(arr)-1):
        if arr[i]!=arr[i-1]:
            arr[write_index]=arr[i]
            write_index+=1

    return write_index  #new_lenght


arr=[1,2,3,4,4,4,5,6,6,6]
print(f'The updated array after removing duplicates method 1 is {RemoveDuplicate_method1(arr)}')
new_lenght=RemoveDuplicate_method2(arr)
print(f'The updated array after removing duplicates method 2 is {arr[:new_lenght]}')