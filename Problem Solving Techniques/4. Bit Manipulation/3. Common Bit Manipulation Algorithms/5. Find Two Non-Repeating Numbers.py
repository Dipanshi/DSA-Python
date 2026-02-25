    # Find two numbers that appear once
    # All others appear twice
def find_two_unique(arr):
    xor_all=0
    for i in arr:
        xor_all^=i
    first=second=0
    rightmost=xor_all & -xor_all
    for i in arr:
        if i&rightmost:
            first^=i
        else:
            second^=i
    
    return first,second

num=[1,2,3,5,6,4,1,2,3,6]
print(find_two_unique(num))