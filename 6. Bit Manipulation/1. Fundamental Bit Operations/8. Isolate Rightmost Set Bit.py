def isolate_rightmost_set_bit(num):
    """Get only the rightmost set bit"""
    return num & -num

# Examples:
# 12 (1100) -> 4 (0100)
print(isolate_rightmost_set_bit(12))
# 10 (1010) -> 2 (0010)
print(isolate_rightmost_set_bit(10))