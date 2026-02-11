#    Count triplets (i,j,k) where arr[i]^arr[i+1]^...^arr[j-1] == arr[j]^...^arr[k]
#     Time: O(n²), Space: O(n)

def count_triplets_xor_zero(arr):
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    
    for i in range(n):
        prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
    
    count = 0
    for i in range(n):
        for k in range(i+1, n):
            if prefix_xor[i] == prefix_xor[k+1]:
                count += k - i
    
    return count

# Test:
print(count_triplets_xor_zero([2, 3, 1, 6, 7]))  # 4