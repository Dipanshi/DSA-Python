# Find Second largest element from array

def SecondLargestElement(arr):
    if len(arr)<2:
        return None
    first,second= float('-inf'),float('-inf')
    for a in arr:
        if a>first:
            second=first
            first=a
        elif a>second and a!=first:
            second=a
    
    return second if second!=float('-inf') else None

arr=[10,2,6,9,30,20,1,4,7]
print(f'The Second Element in array is {SecondLargestElement(arr)}')