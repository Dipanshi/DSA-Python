 #Find Maximum and Minimum
"""Find min and max in single pass - O(n)"""

def Min_Max(arr):
    if arr is None:
        return None,None
    min_val=max_val=arr[0]
    for a in arr:
        if min_val>a:
            min_val=a
        if max_val<a:
            max_val=a
    return min_val,max_val

if __name__=="__main__":
    min_val,max_val=Min_Max([10,1,3,5,6,7,4,5,2,15])
    print(f"Min value in the array is {min_val}")
    print(f"Max value in the array is {max_val}")