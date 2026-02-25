    # Find length of longest subarray with sum k
    # Time: O(n), Space: O(n)

def longest_subarray_sum_k(nums, k):
    max_index={0:-1}
    max_len=0
    prefix_sum=0
    for i,num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum-k in max_index:
            max_len=max(max_len,i-max_index[prefix_sum-k ])
        
        if prefix_sum not in max_index:
            max_index[prefix_sum]=i
    return max_len

print(longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15))  #4