# You are given:
# An array of non-negative integers
# Each number represents the height of a bar
# Each bar has width = 1
# Your task: Calculate how much rain water can be trapped between the bars after it rains.
#height = [0,1,0,2,1,0,1,3,2,1,2,1]

def TrappingRainWater(height):
    left_max,right_max,water=0,0,0
    left,right=0,len(height)-1
    while left<right:
        if height[left]<height[right]:
            if height[left]>=height[left_max]:
                height[left_max]=height[left]
            else:
                water += height[left_max]-height[left]
            left+=1
        else:
            if height[right]>=height[right_max]:
                height[right_max]=height[right]
            else:
                water+=height[right_max]- height[right]
            right-=1
    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(TrappingRainWater(height))