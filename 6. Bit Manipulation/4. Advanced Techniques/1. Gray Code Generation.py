def gray_code(n):
    """Generate n-bit Gray code sequence"""
    result = []
    for i in range(1 << n):
        # Gray code: i ^ (i >> 1)
        result.append(i ^ (i >> 1))
    return result

# Examples:
print(gray_code(2))  # [0, 1, 3, 2]
print(gray_code(3))  # [0, 1, 3, 2, 6, 7, 5, 4]

# Gray code property: successive values differ by 1 bit