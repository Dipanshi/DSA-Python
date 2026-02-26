# Distribute elements into buckets, sort each bucket, concatenate.

def bucket_sort(arr):
    """
    Bucket Sort - Distribution based
    Time: O(n + k) average, O(n²) worst
    Space: O(n + k)
    Stable: Depends on bucket sorting algorithm
    Works best with uniformly distributed data
    """
    if not arr:
        return arr
    
    # Create buckets
    n = len(arr)
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / n
    
    buckets = [[] for _ in range(n)]
    
    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == n:  # Handle max value
            index = n - 1
        buckets[index].append(num)
    
    # Sort each bucket and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))  # Can use any sorting algorithm
    
    return result

# Test
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Sorted:", bucket_sort(arr))
# Output: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]