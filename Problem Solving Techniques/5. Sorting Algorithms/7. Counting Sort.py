# Count occurrences of each element, use counts to place elements in sorted order.
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)
    
    return result


# Test
arr = [4, 2, 2, 8, 3, 3, 1]
print("Sorted:", counting_sort(arr))
# Output: [1, 2, 2, 3, 3, 4, 8]
