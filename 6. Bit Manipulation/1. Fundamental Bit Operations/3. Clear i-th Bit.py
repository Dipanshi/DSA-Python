def clear_bit(num, i):
    """Clear i-th bit (set to 0)"""
    return num & ~(1 << i)

# Examples:
num = 13  # 1101
print(clear_bit(num, 0))  # 1100 = 12
print(clear_bit(num, 2))  # 1001 = 9

