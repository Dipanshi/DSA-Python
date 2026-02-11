def inplacesum(num):
    for i in range(1, len(num)):
        num[i]+=num[i-1]

    return num

num=[2,4,5,6,7,2,8,9]
print(inplacesum(num))