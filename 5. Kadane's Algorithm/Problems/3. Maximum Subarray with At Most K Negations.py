    # Maximize sum after flipping at most k numbers
    # Time: O(n log n), Space: O(1)

def max_sum_after_k_negations(nums, k):
    nums.sort()
    for i in range(len(nums)):
        if k>0 and nums[i]<0:
            nums[i]=-nums[i]
            k-=1
    if k%2==1:
        nums.sort()
        nums[0]=-nums[0]
    
    return sum(nums)

print(max_sum_after_k_negations([4, 2, 3], 1))     # 5
print(max_sum_after_k_negations([3, -1, 0, 2], 3)) # 6
        