def swap_xor(a, b):
    a = a ^ b
    b = a ^ b  # b = (a^b) ^ b = a
    a = a ^ b  # a = (a^b) ^ a = b
    return a, b


print(swap_xor(12,34))