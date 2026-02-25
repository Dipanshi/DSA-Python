def get_set_bit_position(n):
    """Find position of the only set bit"""
    if n == 0 or (n & (n - 1)) != 0:
        return -1  # Not exactly one bit set
    
    pos = 0
    while n > 1:
        n >>= 1
        pos += 1
    
    return pos


print(get_set_bit_position(8))   # 3 (1000)
print(get_set_bit_position(16))  # 4 (10000)