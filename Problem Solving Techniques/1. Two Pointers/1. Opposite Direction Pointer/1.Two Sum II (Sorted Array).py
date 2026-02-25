    # Find two numbers that add up to target in sorted array
    # Time: O(n), Space: O(1)

def TwoSumII(numbers,target):
    left,right=0,len(numbers)-1
    total=0
    while left<right:
        total= numbers[left]+numbers[right]
        if total==target:
            return [numbers[left],numbers[right]]
        elif total<target:
            left+=1
        else:
            right-=1
    return None   

Numbers= [2, 7, 11, 15]
Target= 9
print(TwoSumII(Numbers,Target))