    # Calculate how much rain water can be trapped
    # Time: O(n), Space: O(1)

def rain_water_trap(height):
    if not height:
        return None
    
    left,right=0,len(height)-1
    left_max,right_max=0,0
    water=0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                water += left_max-height[left]
            left +=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                water+= right_max-height[right]
            right-=1

    return water
    
print(rain_water_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6

