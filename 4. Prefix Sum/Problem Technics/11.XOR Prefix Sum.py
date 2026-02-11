    # Build prefix XOR array
    # Time: O(n), Space: O(n)
def XORPrefix(nums):
    n= len(nums)
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]^nums[i]
    
    return prefix

arr = [1, 3, 4, 8]
prefix_xor = XORPrefix(arr)
print(prefix_xor)  # [0, 1, 2, 6, 14]

# XOR from index 1 to 3
print(prefix_xor[4] ^ prefix_xor[1])  # 3^4^8 = 15