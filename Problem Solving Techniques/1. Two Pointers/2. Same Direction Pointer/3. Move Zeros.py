    # Move all zeros to end while maintaining order
    # Time: O(n), Space: O(1)

def MoveZero(nums):
    if not nums:
        return None
    slow=0
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow],nums[fast]=nums[fast],nums[slow]
            slow+=1

    return nums

print(MoveZero([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
