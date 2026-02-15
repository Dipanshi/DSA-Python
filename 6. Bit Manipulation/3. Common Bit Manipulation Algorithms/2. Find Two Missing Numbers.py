Revisit

def find_two_missing(arr, n):
    """Find two missing numbers from 1 to n"""
    # XOR of all numbers and array elements
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in arr:
        xor_all ^= num
    
    # xor_all = missing1 ^ missing2
    # Find rightmost set bit
    rightmost_set = xor_all & -xor_all
    #print(rightmost_set)
    # Divide numbers into two groups
    missing1 = missing2 = 0
    
    for i in range(1, n + 1):
        if i & rightmost_set:
            missing1 ^= i
        else:
            missing2 ^= i
    #    print(f" loop 1 in {missing1,missing2}")    
    for num in arr:
        if num & rightmost_set:
            missing1 ^= num
        else:
            missing2 ^= num
      #  print(f" loop 2 in {missing1,missing2}")
    
    return missing1, missing2


num=[1,3,4,5,7,8]
print(find_two_missing(num,8))