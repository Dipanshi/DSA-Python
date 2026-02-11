    # Build suffix sum array
    # suffix[i] = sum of elements from index i to end
    # Time: O(n), Space: O(n)

def SuffixSum(num):
    n=len(num)
    res_num=[0]*len(num)
    res_num[-1]=num[-1]
    for i in range(n-2,-1,-1):
        res_num[i]= res_num[i+1]+num[i]

    return res_num

arr = [3, 1, 4, 1, 5, 9, 2, 6]
suffix = SuffixSum(arr)
print(suffix)  # [31, 28, 27, 23, 22, 17, 8, 6]