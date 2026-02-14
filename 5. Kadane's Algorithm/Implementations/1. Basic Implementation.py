    # Find maximum sum of contiguous subarray (Kadane's Algorithm)
    # Time: O(n), Space: O(1)

def max_subarray_sum(nums):
    if not nums:
        return 0
    current_sum=0
    max_sum=0
    for num in nums:
        current_sum = max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_sum([1]))                                # 1
print(max_subarray_sum([5, 4, -1, 7, 8]))                  # 23
