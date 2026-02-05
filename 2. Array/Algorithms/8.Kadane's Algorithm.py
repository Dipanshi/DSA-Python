#Kadane's Algorithm (Maximum Subarray Sum)
# +ve and +ve will be +ve
# -ve and +ve can be +ve
# but -ve and -ve or very big -ve and +ve will be -ve only.
#  which is the concept use in this algo that if -ve make it 0 as it can be max.
"""Find maximum sum of contiguous subarray - O(n)"""
# Way one to write.
def kadaneAlgo(arr):
    curr_val = 0
    max_val = float('-inf')

    for i in arr:
        curr_val +=i
        max_val= max(max_val,curr_val)
        if curr_val<0:
            curr_val=0
    
    return max_val

# Way one to write.
def kadaneAlgo1(arr):
    max_val=curr_val = arr[0]

    for a in arr[1:]:
        curr_val = max(a,curr_val+a)
        max_val= max(max_val,curr_val)    
    return max_val

arr = [1,2,-2,3,-4,-1,8,-1,6]
arr2= [-9,-4,-5,-6,-7,-1]
print(f'The maximum sum is {kadaneAlgo(arr2)}')
print(f'The maximum sum is {kadaneAlgo1(arr2)}')

