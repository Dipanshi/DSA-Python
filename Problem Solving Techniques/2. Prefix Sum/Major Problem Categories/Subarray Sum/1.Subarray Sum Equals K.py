    # Count subarrays with sum equal to k
    # Time: O(n), Space: O(n)
def subarray_sum_k(nums, k):
    prefix_sum=0
    sum_count={0:1}
    count=0
    for num in nums:
        prefix_sum+=num
        if prefix_sum-k in sum_count:
            count+=sum_count[prefix_sum-k]
      
        sum_count[prefix_sum]= sum_count.get(prefix_sum,0)+1
    
    return count

print(subarray_sum_k([1, 1, 1], 2))      # 2
print(subarray_sum_k([1, 2, 3], 3))      # 2
print(subarray_sum_k([1, -1, 0], 0))     # 3