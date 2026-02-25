# Method 1: Brian Kernighan's Algorithm - O(number of set bits)
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

# Method 2: Using built-in - O(1)
def count_set_bits_builtin(n):
    return bin(n).count('1')

# Method 3: Bit by bit - O(log n)
def count_set_bits_v3(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Examples:
print(count_set_bits(13))  # 1101 -> 3
print(count_set_bits(7))   # 0111 -> 3