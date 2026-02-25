def longest_consecutive_ones(n):
    """Find length of longest consecutive 1's in binary"""
    count = 0
    max_count = 0
    
    while n:
        if n & 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1
    
    return max_count

# Examples:
print(longest_consecutive_ones(14))   # 1110 -> 3
print(longest_consecutive_ones(222))  # 11011110 -> 4