# Set i-th bit to 1

def set_bit(num, i):
    return num | (1 << i)


# Examples:
num = 8   # 1000
print(set_bit(num, 0))  # 1001 = 9
print(set_bit(num, 2))  # 1100 = 12