def clear_rightmost_set_bit(num):
    """Clear the rightmost set bit"""
    return num & (num - 1)

# Examples:
# 12 (1100) -> 8 (1000)
print(clear_rightmost_set_bit(12))
# 10 (1010) -> 8 (1000)
print(clear_rightmost_set_bit(10))
# 7  (0111) -> 6 (0110)
print(clear_rightmost_set_bit(7))

# This is used to count set bits!