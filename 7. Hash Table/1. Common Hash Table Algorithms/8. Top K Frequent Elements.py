    # Find k most frequent elements
    # O(n) time using bucket sort


def top_k_frequent(nums, k):
    res=[]
    count_index={}
    for n in nums:
        count_index[n]=count_index.get(n,0)+1
    for i in count_index.keys():
        if count_index[i]>=k:
            res.append(i)
    return res

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(top_k_frequent([1], 1))                  # [1]