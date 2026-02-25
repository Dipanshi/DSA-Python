#  Check if i-th bit (0-indexed from right) is set

def is_bit_set(num, i):
    return (num & (1<<i))!=0


# Examples:
num = 13  # 1101
print(is_bit_set(num, 0))  # True  (bit 0 is 1)
print(is_bit_set(num, 1))  # False (bit 1 is 0)
print(is_bit_set(num, 2))  # True  (bit 2 is 1)
print(is_bit_set(num, 3))  # True  (bit 3 is 1)


# Alternative: using boolean
def is_bit_set_bool(num, i):
    return bool(num & (1 << i))