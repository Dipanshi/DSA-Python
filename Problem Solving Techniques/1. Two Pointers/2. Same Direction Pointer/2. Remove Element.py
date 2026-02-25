    # Remove all occurrences of val in-place
    # Time: O(n), Space: O(1)
def remove_element(nums, val):
    slow=0
    for fast in range(len(nums)):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            slow+=1
    
    return nums[:slow+1]
print(remove_element([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],1))

