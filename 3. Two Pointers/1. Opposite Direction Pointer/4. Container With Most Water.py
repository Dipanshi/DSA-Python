#    Find two lines that form container with most water
    # Time: O(n), Space: O(1)
def maxarea(height):
    left,right=0,len(height)-1
    max_area=0
    while left<right:
        w=right-left
        h=min(height[left],height[right])
        area=w*h
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
        max_area=max(max_area,area)
    return max_area

print(maxarea([1, 8, 6, 2, 5, 4, 8, 3, 7]))