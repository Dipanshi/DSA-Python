# Multiply by 2^n
def multiply_by_power_2(num, n):
    return num << n

# Divide by 2^n
def divide_by_power_2(num, n):
    return num >> n

# Examples:
print(multiply_by_power_2(5, 2))  # 5 * 4 = 20
print(divide_by_power_2(20, 2))   # 20 / 4 = 5

# Faster than num * (2**n) or num // (2**n)