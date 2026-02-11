def RangeSumQuery(nums,l,r):
    pre_sum=[0]*len(nums)
    pre_sum[0]=nums[0]
    for i in range(1,len(nums)):
        pre_sum[i] = pre_sum[i-1]+nums[i]
    
    return pre_sum[r]-pre_sum[l-1]


nums=[1,3,2,6,3,7,4,6]
print(RangeSumQuery(nums,3,6))

