# Apply range updates efficiently
# Difference Array Technique (Used in Range Addition Problems)
# The difference array technique is an optimization method used to perform multiple range updates efficiently.
# Instead of updating every element in a range (which takes O(n) per update),
# we mark only the boundaries and compute the final array later using prefix sums.
    # Time: O(n + k), Space: O(n)


def range_addition(length, updates):
    res= [0]*length
    for start,end,value in updates:
        res[start]+=value
        if end+1<length:
            res[end+1]-=value

    for i in range(1,length):
        res[i]+=res[i-1]

    return res

n = 5
updates = [[1, 3, 2],[2, 4, 3],[0, 2, -2]]
print(range_addition(n,updates))

