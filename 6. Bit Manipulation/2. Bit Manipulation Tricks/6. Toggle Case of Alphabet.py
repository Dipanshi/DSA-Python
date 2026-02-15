def toggle_case(char):
    """Toggle between uppercase and lowercase"""
    # XOR with space (32 = 0b100000)
    return chr(ord(char) ^ 32)

# Examples:
print(toggle_case('A'))  # 'a'
print(toggle_case('a'))  # 'A'
print(toggle_case('Z'))  # 'z'

# Works because:
# 'A' = 65 = 01000001
# 'a' = 97 = 01100001
# Difference is bit 5 (32)