def is_power_of_two(n):
    """
    Power of 2 has only one bit set
    n:     1000
    n-1:   0111
    n&(n-1): 0000
    """
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))
print(is_power_of_two(6))
print(is_power_of_two(32))

