def count_bits_range(num):
    result = [0] * (num + 1)
    
    for i in range(1, num + 1):
        result[i] = result[i & (i - 1)] + 1
    
    return result

# Examples:
print(count_bits_range(5))  # [0, 1, 1, 2, 1, 2]
# 0: 0000 -> 0
# 1: 0001 -> 1
# 2: 0010 -> 1
# 3: 0011 -> 2
# 4: 0100 -> 1
# 5: 0101 -> 2