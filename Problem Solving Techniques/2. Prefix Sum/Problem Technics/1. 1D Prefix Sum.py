def PrefixSum(nums):
    n=len(nums)
    for i in range(1,n):
        nums[i]+=nums[i-1]
    
    return nums

nums=[1,4,2,6,4,7,3]
print(PrefixSum(nums))


