    # Find two numbers that add up to target
    # O(n) time, O(n) space

def two_sum(nums, target):
    if len(nums)<2:
        return []
    sum_index={0:-1}
    for i,num in enumerate(nums):
        if target-num in sum_index:
            return [nums[sum_index[target-num]],num]
        sum_index[num]=i
    return []


num=[1,2,4,6,7,8,9,5]
target=11
print(two_sum(num,target))
