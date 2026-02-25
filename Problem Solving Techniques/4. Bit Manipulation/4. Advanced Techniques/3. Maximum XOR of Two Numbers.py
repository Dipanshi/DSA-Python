def find_max_xor(arr):
    """Find maximum XOR of two numbers in array"""
    max_xor = 0
    mask = 0
    
    # Try from most significant bit to least
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = set()
        
        # Get all prefixes
        for num in arr:
            prefixes.add(num & mask)
        
        # Try to find if max_xor | (1 << i) is achievable
        temp = max_xor | (1 << i)
        
        for prefix in prefixes:
            if temp ^ prefix in prefixes:
                max_xor = temp
                break
    
    return max_xor

# O(n^2) brute force
def find_max_xor_brute(arr):
    max_xor = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_xor = max(max_xor, arr[i] ^ arr[j])
    return max_xor