# Count subarrays with sum divisible by k
#     Time: O(n), Space: O(k)

def subarrays_div_by_k(nums, k):
    prefix_sum=0
    reminder_index={0:1}
    count=0
    for num in nums:
        prefix_sum+=num
        reminder=prefix_sum%k
        if reminder<0:
            reminder+=k
        count+= reminder_index.get(reminder,0)
        reminder_index[reminder]=reminder_index.get(reminder,0)+1
    return count


print(subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))  # 7