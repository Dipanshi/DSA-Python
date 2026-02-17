    # Count subarrays with sum equal to k
    # O(n) time, O(n) space

def subarray_sum_k(nums, k):
    total_subs=0
    prefix_sum=0
    res_sum={0:1}
    for num in nums:
        prefix_sum+=num
        if prefix_sum-k in res_sum:
            total_subs+=res_sum[prefix_sum-k]

        res_sum[prefix_sum]=res_sum.get(prefix_sum,0)+1
    return total_subs

print(subarray_sum_k([1, 1, 1], 2))      # 2
print(subarray_sum_k([1, 2, 3], 3))      # 2
print(subarray_sum_k([1, -1, 0], 0))     # 3
