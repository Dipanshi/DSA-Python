    # Find maximum length of subarray with sum k
    # Time: O(n), Space: O(n)

def max_subarray_len(nums, k):
    max_len= 0
    sum_index={0:-1}
    prefix_sum=0
    for i, num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum-k in sum_index:
            max_len=max(max_len,i-sum_index[prefix_sum-k])
        
        if prefix_sum not in sum_index:
            sum_index[prefix_sum]=i

    return  max_len

print(max_subarray_len([1, -1, 5, -2, 3], 3))   # 4
print(max_subarray_len([-2, -1, 2, 1], 1))      # 2

