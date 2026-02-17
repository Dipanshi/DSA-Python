    # Find length of longest consecutive sequence
    # O(n) time, O(n) space

def longest_consecutive(nums):
    max_lenght=lenght=0
    set_num=set()
    for num in nums:
        n=num
        while n not in set_num and n+1 in nums:
            set_num.add(n)
            lenght+=1
            n+=1
        max_lenght=max(max_lenght,lenght+1)

    return max_lenght


num=[100, 4, 200, 1, 3, 2]
print(longest_consecutive(num))
print(longest_consecutive([0, -1, 1, 2, -2, 3]))
print(longest_consecutive([1, 2, 0, 1]))