#    Find maximum absolute value of sum
#     Time: O(n), Space: O(1)

def max_absolute_sum(nums):
    max_pos=max_sum=0
    min_neg=min_sum=0
    for num in nums:
        max_pos= max(0,max_pos+num)
        max_sum=max(max_sum,max_pos)
        min_neg=min(0,min_neg+num)
        min_sum=min(min_sum,min_neg)

    return max(max_sum,abs(min_sum))

print(max_absolute_sum([1, -3, 2, 3, -4]))  # 5
print(max_absolute_sum([2, -5, 1, -4, 3, -2]))  # 8