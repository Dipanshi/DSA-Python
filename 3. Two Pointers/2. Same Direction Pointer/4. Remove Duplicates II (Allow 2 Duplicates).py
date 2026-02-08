#    Remove duplicates so each element appears at most twice
#     Time: O(n), Space: O(1)
def removeDuplicateII(nums):
    if len(nums)<=2:
        return nums
    slow=2
    for fast in range(2,len(nums)):
        if nums[fast]!=nums[slow-2]:
            nums[slow]=nums[fast]
            slow+=1

    return nums[:slow+1]
    
nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicateII(nums))
