    # Find all unique triplets that sum to zero
    # Time: O(n²), Space: O(1) excluding output
def threesum(arr):
    arr.sort()
    result=[]
    for i  in range(len(arr)-2):
       #skip if first number is duplicate
       if i>0 and arr[i]==arr[i-1]: 
           continue
       
       left,right=i+1,len(arr)-1
       target=-arr[i]
       while left<right:
           current=arr[left]+arr[right]
           if current==target:
               result.append([arr[i],arr[left],arr[right]])
               # Check is left or right is duplicate and skip them to avoid creating duplicate subarray
               while left<right and  arr[left]==arr[left+1]:
                   left+=1
               while left<right and  arr[right]==arr[right-1]:
                  right-=1
               left+=1
               right-=1
               
           elif target<current:
                   left+=1
           else:
               right-=1
    return result
                   
            
           
print(threesum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
