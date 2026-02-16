def count_total_set_bits(n):
    """Count total set bits in all numbers from 1 to n"""
    count = 0
    power_of_2 = 1
    
    while power_of_2 <= n:
        # Count complete pairs
        total_pairs = (n + 1) // (power_of_2 * 2)
        count += total_pairs * power_of_2
        
        # Count remaining
        remainder = (n + 1) % (power_of_2 * 2)
        if remainder > power_of_2:
            count += remainder - power_of_2
        
        power_of_2 <<= 1
    
    return count

# Simple O(n log n) approach
def count_total_set_bits_simple(n):
    count = 0
    for i in range(1, n + 1):
        count += bin(i).count('1')
    return count