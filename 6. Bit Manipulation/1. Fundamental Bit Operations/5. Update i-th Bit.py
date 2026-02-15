def update_bit(num, i, value):
    """Update i-th bit to given value (0 or 1)"""
    # Clear the bit first, then set if value is 1
    mask = ~(1 << i)
    return (num & mask) | (value << i)

# Alternative shorter version:
def update_bit_v2(num, i, value):
    return (num & ~(1 << i)) | (value << i)

# Examples:
num = 13  # 1101
num = update_bit(num, 1, 1)
print(num)  # 1111 = 15
num = update_bit(num, 3, 0)
print(num)  # 0111 = 7