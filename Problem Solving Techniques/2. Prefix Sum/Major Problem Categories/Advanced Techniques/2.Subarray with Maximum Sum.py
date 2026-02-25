    # Find maximum sum of contiguous subarray (Kadane's Algorithm)
    # Time: O(n), Space: O(1)

def max_subarray_sum(nums):
    max_sum=0
    prefix_sum=0
    for num in nums:
        prefix_sum+=num
        prefix_sum= max(prefix_sum,num)
        max_sum=max(max_sum,prefix_sum)
    return max_sum

def max_subarray_with_indices(nums):
    """Return max sum with start and end indices"""
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_with_indices([5, -3, 5]))  # (7, 0, 2)
