# Remove Duplicate (Unsorted Array)
"""Remove duplicates maintaining order - O(n)"""

def RemoveDuplicate(arr):
    seen=set()
    res=[]
    for i in arr:
        if i not in seen:
            seen.add(i)
            res.append(i)
    return res

arr=[1,2,4,2,1,3,5,7,9,7]
print(f'The updated array is {RemoveDuplicate(arr)}')
