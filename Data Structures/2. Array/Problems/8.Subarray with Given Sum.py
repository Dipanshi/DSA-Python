# Determine whether there exists a contiguous subarray whose sum equals S
# (or sometimes: return the subarray / its indices)
# Array = [1, 2, 3, 7, 5]
# Target Sum = 12

def SubarrayGivenArray(arr,target):
    current_sum = 0
    sum_map = {0:-1}
    for i,num in enumerate(arr):
        current_sum+=num
        if current_sum-target in sum_map:
            start = sum_map[current_sum-target]+1
            return arr[start:i+1]
        sum_map[current_sum]=i

    return None
    
Array = [1, 2, 3, 7, 5]
Target = 12
print(SubarrayGivenArray(Array,Target))








