def equilibrium_index(arr):
    """
    Find index where left sum equals right sum
    Time: O(n), Space: O(1)
    """
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        # Right sum = total - left_sum - current
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]
    
    return -1

# Test:
print(equilibrium_index([1, 3, 5, 2, 2]))  # 2 (1+3 == 2+2)
print(equilibrium_index([1, 2, 3]))  