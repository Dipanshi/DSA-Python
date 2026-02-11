    # Find maximum product of contiguous subarray
    # Time: O(n), Space: O(1)

def MaxProduct(num):
    max_val=0
    max_prod=1
    for i in range(len(num)):
        max_prod*=num[i]
        max_val=max(max_val,max_prod)

    return max_val


print(MaxProduct([2, 3, -2, 4]))     # 6
print(MaxProduct([-2, 0, -1]))       # 0
print(MaxProduct([-2, 3, -4]))       # 24