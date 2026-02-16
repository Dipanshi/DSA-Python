def find_two_missing(arr, n):
    xor_all=0
    for i in range(1,n+1):
        xor_all^=i
    for i in arr:
        xor_all^=i
    #xor_all= missing1 ^ missing2
    missing1=missing2=0
    rightmost=xor_all & -xor_all
    for i in range(1,n+1):
        if i&rightmost:
            missing1^=i
        else:
            missing2^=i
    for i in arr:
        if i&rightmost:
            missing1^=i
        else:
            missing2^=i

    return missing1,missing2
    

num=[1,3,4,5,7,8]
print(find_two_missing(num,8))