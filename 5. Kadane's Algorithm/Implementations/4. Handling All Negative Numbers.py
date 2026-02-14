    # Handle case when all numbers are negative
    # Time: O(n), Space: O(1)

def max_subarray_all_negative(nums):
    current= max_sum=float('-inf')
    for num in nums:
        current= max(num,current+num)
        max_sum=max(max_sum,current)
    return max_sum

print(max_subarray_all_negative([-5, -2, -8, -1, -4]))  # -1