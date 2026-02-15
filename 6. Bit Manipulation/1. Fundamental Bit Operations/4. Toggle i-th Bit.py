def toggle_bit(num, i):
    """Flip i-th bit (0->1, 1->0)"""
    return num ^ (1 << i)

# Examples:
num = 13  # 1101
num = toggle_bit(num, 0)
print(num)  # 1100 = 12
num = toggle_bit(num, 1)
print(num)  # 1110 = 14
num = toggle_bit(num, 1)
print(num)  # 1100 = 12 (toggle back)