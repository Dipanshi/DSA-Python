    # Sort array with values 0, 1, 2 in-place
    # Time: O(n), Space: O(1)
def sort_color(color):
    start,middle,end=0,0,len(color)-1
    while middle<=end:
        if color[middle]==2:
            color[end],color[middle]=color[middle],color[end]
            end-=1
        elif color[middle]==0:
            color[start],color[middle]=color[middle],color[start]
            start+=1
            middle+=1
        else:
            middle+=1
    return color

print(sort_color([1,0,2,2,1,2,1,0,0,0,1]))