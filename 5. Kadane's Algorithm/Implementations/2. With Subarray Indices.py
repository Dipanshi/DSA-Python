    # Return maximum sum with start and end indices
    # Time: O(n), Space: O(1)

def max_subarray_with_indices(nums):
    if not nums:
        return 0  
    start=end=temp_start=0
    max_sum=current_sum=0
    for i,num in enumerate(nums):
        if num>current_sum+num:
            current_sum=num
            temp_start=i
        else:
            current_sum+=num
        if max_sum<current_sum:
            max_sum=current_sum
            start= temp_start
            end=i
    return max_sum,start,end


print(max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray_with_indices([1]))                                # 1
print(max_subarray_with_indices([5, 4, -1, 7, 8]))                  # 23