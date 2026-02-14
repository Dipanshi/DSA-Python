
    # Find maximum length subarray with equal 0s and 1s
    # Time: O(n), Space: O(n)

def find_max_length(nums):
    sum_index={0:-1}
    max_lenght=0
    prefix_sum=0
    for i,num in enumerate(nums):
        num=-1 if num==0 else num
        prefix_sum+=num
        if prefix_sum in sum_index:
            max_lenght= max(max_lenght, i - sum_index[prefix_sum])
        else:
            sum_index[prefix_sum]=i
    return max_lenght

print(find_max_length([0, 1]))           # 2
print(find_max_length([0, 1, 0]))        # 2
print(find_max_length([0, 1, 1, 0, 1]))  # 4

