    # Calculate difference between left and right sums
    # Time: O(n), Space: O(n)
def PrefixSuffixSum(num):
    n=len(num)
    res=[0]*n
    left=0
    for i in range(n):        
        left+=num[i]
        res[i]= left
        
    right=0
    for i in range(n-1,-1,-1): 
        right+=num[i]
        res[i]=abs(res[i]-right) 
        
    
    return res


# Test:
print(PrefixSuffixSum([10, 4, 8, 3]))  # [15, 1, 11, 22]