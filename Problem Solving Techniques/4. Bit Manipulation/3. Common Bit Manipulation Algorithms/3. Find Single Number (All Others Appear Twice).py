def Single_Number(nums):
    xor_all=0
    for num in nums:
        xor_all^=num
    return xor_all

nums=[1,2,4,5,6,7,3,1,2,4,5,6,7]
print(Single_Number(nums))
