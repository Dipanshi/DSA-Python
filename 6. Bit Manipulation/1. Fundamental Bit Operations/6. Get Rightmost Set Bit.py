def get_rightmost_set_bit(num):
    """Get position of rightmost set bit (1-indexed)"""
    if num == 0:
        return -1
    
    # Method 1: Using & with two's complement
    rightmost = num & -num
    # Find position
    pos = 0
    while rightmost > 1:
        rightmost >>= 1
        pos += 1
    
    return pos

# Alternative: Direct calculation
def rightmost_set_bit_v2(num):
    return (num & -num).bit_length() - 1

# Examples:
print(get_rightmost_set_bit(12))  # 1100 -> position 2
print(get_rightmost_set_bit(10))  # 1010 -> position 1