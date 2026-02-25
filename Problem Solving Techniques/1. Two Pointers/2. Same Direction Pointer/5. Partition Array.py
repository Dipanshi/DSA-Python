    # Partition array around pivot value
    # Time: O(n), Space: O(1)

def partition_array(nums, pivot):

    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] < pivot:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    return slow  

nums = [3, 1, 4, 1, 5, 9, 2, 6]
pivot_index = partition_array(nums, 5)
print(nums) 

