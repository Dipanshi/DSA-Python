# Find minimum sum of contiguous subarray
def min_subarray_sum(nums):
    if not nums:
        return 0
    current= min_sum=0
    for num in nums:
        current= min(num,current+num)
        min_sum= min(current,min_sum)
    return min_sum

print(min_subarray_sum([2, -1, 3, -4, 5]))  # -4
print(min_subarray_sum([1, -3, 2, -5, 4]))  # -5