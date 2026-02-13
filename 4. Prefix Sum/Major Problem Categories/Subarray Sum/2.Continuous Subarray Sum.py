    # Check if array has continuous subarray of size >= 2 with sum multiple of k
    # Time: O(n), Space: O(k)

def check_subarray_sum(nums, k):
    prefix_sum = 0
    remainder_index = {0: -1}  
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if k != 0:
            remainder = prefix_sum % k
        else:
            remainder = prefix_sum
        
        if remainder in remainder_index:
            # Check if subarray size >= 2
            if i - remainder_index[remainder] >= 2:
                return True
        else:
            remainder_index[remainder] = i
    
    return False

# Test:
print(check_subarray_sum([23, 2, 4, 6, 7], 6))    # True
print(check_subarray_sum([23, 2, 6, 4, 7], 13))   # False

