    # Calculate trapped rain water
    # Time: O(n), Space: O(n)

def trap_rain_water(num):
    if not num:
        return 0
    n=len(num)
    left=[0]*n
    left[0]=num[0]
    for i in range(1,n):
        left[i]=max(left[i-1],num[i])
    
    right=[0]*n
    right[-1]=num[-1]
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],num[i])
    water=0
    for i in range(n):
        water+=min(left[i],right[i])-num[i]
    return water

print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6