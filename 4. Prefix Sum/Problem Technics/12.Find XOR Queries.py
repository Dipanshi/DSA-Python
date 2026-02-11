    # Answer multiple XOR range queries
    # Time: O(n + q), Space: O(n)
def xor_queries(arr, queries):
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    
    # Build prefix XOR
    for i in range(n):
        prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
    
    # Answer queries
    result = []
    for left, right in queries:
        result.append(prefix_xor[right+1] ^ prefix_xor[left])
    
    return result

# Test:
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(xor_queries(arr, queries))  # [2, 7, 14, 8]