# You are given:
# An unsorted array of integers
# Numbers can be in any order
# There may be duplicates
# Your task:Find the length of the longest sequence of consecutive integers.

def LongestSequence(arr):
    max_length=0
    sets=set()
    for num in arr:
        s,length=num,1
        while s+1 in arr and s not in sets:
            length+=1
            s+=1
            sets.add(num)
        max_length=max(max_length,length)

    return max_length

nums = [-2, -1, 0, 1]
print(LongestSequence(nums))