from collections import deque

def max_sliding_window(nums, k):
    """
    Find max in each sliding window
    Time: O(n), Space: O(k)
    """
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Test:
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]