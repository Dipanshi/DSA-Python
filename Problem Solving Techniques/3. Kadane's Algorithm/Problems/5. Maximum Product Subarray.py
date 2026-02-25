    # Find maximum product of contiguous subarray
    # Track both max and min (negative * negative = positive)
    # Time: O(n), Space: O(1)

def max_product_subarray(nums):
    max_prd=min_prd=res=nums[0]
    for num in nums[1:]:
        if num<0:
            min_prd,max_prd=max_prd,min_prd
        max_prd = max(num,max_prd*num)
        min_prd= min(num,min_prd*num)
        res= max(res,max_prd)
    
    return res

print(max_product_subarray([2, 3, -2, 4]))     # 6
print(max_product_subarray([-2, 0, -1]))       # 0
print(max_product_subarray([-2, 3, -4]))       # 24