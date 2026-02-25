    # Find missing number from 1 to n
    # Using XOR: a ^ a = 0, a ^ 0 = a

def find_missing_number(arr, n):
    xor_all=0
    for i in range(1,n+1):
        xor_all^=i
    for i in arr:
        xor_all^=i
    return xor_all

nums=[1,3,4,5,6,7]
print(find_missing_number(nums,7))


# Optimized version
def find_missing_number_v2(arr, n):
    xor_result = 0
    
    for i in range(len(arr)):
        xor_result ^= arr[i] ^ (i + 1)
    
    xor_result ^= n
    return xor_result