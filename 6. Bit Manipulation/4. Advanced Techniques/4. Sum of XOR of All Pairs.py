def xor_all_pairs(arr):
    """
    Find XOR of all pairs: arr[i] ^ arr[j] for all i < j
    Key insight: Each bit contributes independently
    """
    n = len(arr)
    result = 0
    
    # For each bit position
    for i in range(32):
        count_ones = 0
        
        # Count numbers with i-th bit set
        for num in arr:
            if num & (1 << i):
                count_ones += 1
        
        count_zeros = n - count_ones
        
        # Contribution = count_ones * count_zeros * 2^i
        result += (count_ones * count_zeros) * (1 << i)
    
    return result