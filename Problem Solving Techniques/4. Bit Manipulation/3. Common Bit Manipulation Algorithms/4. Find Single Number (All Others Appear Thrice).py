def single_number_thrice(arr):
    """
    Find number that appears once
    All others appear three times
    """
    ones = twos = 0
    
    for num in arr:
        # Update twos with bits that appeared twice
        twos |= ones & num
        
        # Update ones with current number
        ones ^= num
        
        # Remove bits that appeared three times
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    
    return ones

# Alternative: Count bits approach
def single_number_thrice_v2(arr):
    result = 0
    
    for i in range(32):
        bit_sum = 0
        for num in arr:
            if num & (1 << i):
                bit_sum += 1
        
        if bit_sum % 3:
            result |= (1 << i)
    
    return result


num=[1,2,3,4,1,2,3,4,5,1,2,3,4]
print(single_number_thrice(num))