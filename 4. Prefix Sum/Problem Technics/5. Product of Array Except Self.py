def ProductArrayExceptSelf(num):
    res_num=[1]*len(num)
    left=1
    for i in range(len(num)):
        res_num[i]=left
        left*=num[i]
    
    right=1
    for i in range(len(num)-1,-1,-1):
        res_num[i]*=right
        right*=num[i]

    return res_num

print(ProductArrayExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(ProductArrayExceptSelf([2, 3, 4, 5]))  # [60, 40, 30, 24]

