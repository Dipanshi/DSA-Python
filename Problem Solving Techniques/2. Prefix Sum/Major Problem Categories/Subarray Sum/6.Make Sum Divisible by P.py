    # Find minimum subarray to remove so remaining sum divisible by p
    # Time: O(n), Space: O(n)

def min_subarray_to_remove(nums, p):
    total = sum(nums)
    target= total%p
    if target==0:
        return 0
    min_lenght= len(nums)
    count_index={0:-1}
    prefix_sum=0
    for i,num in enumerate(nums):
        prefix_sum+=num
        current= prefix_sum%p
        needed = (current-target+p)%p
        if needed in count_index:
            min_lenght= min(min_lenght,i-count_index[needed])
        count_index[current]=i
    return min_lenght if min_lenght<len(nums) else -1

print(min_subarray_to_remove([3, 1, 4, 2], 6))  # 1
print(min_subarray_to_remove([6, 3, 5, 2], 9))  # 2