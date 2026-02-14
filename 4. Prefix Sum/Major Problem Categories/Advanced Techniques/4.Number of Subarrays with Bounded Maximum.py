    # Count subarrays where max element is in [left, right]
    # Time: O(n), Space: O(1)

def num_subarrays_bounded_max(nums, left, right):

    def count_at_most(bound):
        current=0
        count=0
        for num in nums:
            if num<=bound:
                current+=1
                count+=current
            else:
                current=0

        return count
    
    return count_at_most(right)-count_at_most(left-1)

print(num_subarrays_bounded_max([2, 1, 4, 3], 2, 3))  # 3

