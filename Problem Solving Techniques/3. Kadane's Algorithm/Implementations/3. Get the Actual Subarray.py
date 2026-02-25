    # Return the actual subarray with maximum sum
    # Time: O(n), Space: O(n) for result
def max_subarray_array(nums):
    if not nums:
        return nums
    start=end=temp_start=0
    max_sum=current_sum=0
    for i,num in enumerate(nums):
        if num>current_sum+num:
            current_sum=num
            temp_start=i
        else:
            current_sum+=num
        if current_sum>max_sum:
            max_sum=current_sum
            start=temp_start
            end=i

    return max_sum,nums[start:end+1]


print(max_subarray_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_array([1]))                                # 1
print(max_subarray_array([5, 4, -1, 7, 8]))                  # 23