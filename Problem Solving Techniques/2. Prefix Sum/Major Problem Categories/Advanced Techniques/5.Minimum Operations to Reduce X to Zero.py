    # Find minimum operations to reduce x to 0 by removing from ends
    # Equivalent to finding maximum subarray with sum = total - x
    # Time: O(n), Space: O(n)

def min_operations_reduce_x(nums, x):
    target= sum(nums)-x
    if target<0:
        return -1
    if target==0:
        return len(nums)
    max_len=-1
    prefix_sum=0
    sum_index={0:-1}
    for i, num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum-target in sum_index:
            max_len= max(max_len,i-sum_index[prefix_sum-target])
        sum_index[prefix_sum]= i
    
    return len(nums) - max_len if max_len != -1 else -1

print(min_operations_reduce_x([1, 1, 4, 2, 3], 5))  # 2
print(min_operations_reduce_x([5, 6, 7, 8, 9], 4))  # -1
