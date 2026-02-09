    # Find maximum sum of k consecutive elements
    # Time: O(n), Space: O(1)

def max_sum_subarray(arr, k):
    if len(arr)<k:
        return None
    window_sum = sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum=max(max_sum,window_sum)
    
    return max_sum


print(max_sum_subarray([2, 1, 5, 1, 3, 2],3))
