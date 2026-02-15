def xor_from_1_to_n(n):
    """
    Pattern:
    n % 4 == 0: result = n
    n % 4 == 1: result = 1
    n % 4 == 2: result = n + 1
    n % 4 == 3: result = 0
    """
    remainder = n % 4
    
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else:  # remainder == 3
        return 0

# Examples:
# 1^2^3^4 = 4
# 1^2^3^4^5 = 1
# 1^2^3^4^5^6 = 7

print(xor_from_1_to_n(8))
print(xor_from_1_to_n(3))
print(xor_from_1_to_n(5))
