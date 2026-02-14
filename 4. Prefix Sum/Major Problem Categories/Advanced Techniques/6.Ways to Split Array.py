    # Count ways to split array where left_sum >= right_sum
    # Time: O(n), Space: O(1)

def ways_to_split_array(nums):
    total= sum(nums)
    count=0
    left_sum=0
    for num in nums[:-2]:
        left_sum+=num
        right_sum=total-left_sum
        if left_sum>=right_sum:
            count+=1
    return count

print(ways_to_split_array([10, 4, -8, 7]))  # 2
