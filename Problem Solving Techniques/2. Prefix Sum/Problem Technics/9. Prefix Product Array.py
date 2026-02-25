    # Product of all elements except self
    # Time: O(n), Space: O(1) excluding output

def product_array(nums):
    n=len(nums)
    left,right=1,1
    res=[1]*n
    for i in range(n):
        res[i]=left
        left*=nums[i]
    for i in range(n-1,-1,-1):
        res[i]*=right
        right*=nums[i]

    return res

print(product_array([1, 2, 3, 4]))  # [24, 12, 8, 6]