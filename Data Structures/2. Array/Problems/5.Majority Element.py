#Majority Element (appears > n/2 times)
 # Boyer-Moore Voting Algorithm - O(n) time, O(1) space

def MajorityElement(arr):
    count=0
    candidate=None
    for a in arr:
        if count==0:
            candidate=a
        count+=1 if a==candidate else -1
    return candidate

arr=[1,2,2,5,2,2]
print(MajorityElement(arr))
