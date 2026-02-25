def four_sum_count(nums1, nums2, nums3, nums4):
    """
    Count tuples (i,j,k,l) where nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0
    O(n^2) time, O(n^2) space
    """

    sum_count={}
    count=0
    for a in nums1:
        for b in nums2:
            sumab=a+b
            sum_count[sumab]=sum_count.get(sumab,0)+1

    for c in nums3:
        for d in nums4:
            target=-(c+d)
            if target in sum_count:
                count+=sum_count.get(target,0)

    return count


print(four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))  # 2