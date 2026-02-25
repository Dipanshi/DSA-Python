def power_set(arr):
    """
    Generate all subsets using bit manipulation
    For array of size n, there are 2^n subsets
    """
    n = len(arr)
    total_subsets = 1 << n  # 2^n
    
    result = []
    
    for i in range(total_subsets):
        subset = []
        for j in range(n):
            # Check if j-th bit is set
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    
    return result

# Examples:
arr = [1, 2, 3]
print(power_set(arr))
# [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]