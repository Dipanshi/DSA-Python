    # Check if array has duplicates
    # O(n) time, O(n) space

def contains_duplicate(nums):
    set_num=set(nums)
    if len(nums)==len(set_num):
        return True
    else:
        return False
    

print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False


