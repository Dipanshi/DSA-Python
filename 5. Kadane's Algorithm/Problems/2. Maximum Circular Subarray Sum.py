    # Find max sum in circular array
    # Case 1: Max subarray doesn't wrap around
    # Case 2: Max subarray wraps around (total - min subarray)
    # Time: O(n), Space: O(1)

def max_circular_subarray(nums):
    max_len=max_current=nums[0]
    for num in nums[1:]:
        max_current=max(num,max_current+num)
        max_len=max(max_current,max_len)
    min_len=min_current=nums[0]
    for num in nums[1:]:
        min_current= min(num,min_current+num)
        min_len= min(min_current,min_len)
    
    total= sum(nums)
    max_wrap= total-min_len
    
    if max_wrap==0:
        return max_len
    else:
        return max(max_wrap,max_len)
    
print(max_circular_subarray([1, -2, 3, -2]))      # 3
print(max_circular_subarray([5, -3, 5]))          # 10
print(max_circular_subarray([-3, -2, -3]))        # -2