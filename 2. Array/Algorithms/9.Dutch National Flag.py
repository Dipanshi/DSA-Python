#Dutch National Flag (3-way Partitioning)
#Logic is to arrage all 0's, 1's and 2's in respective.
#set start, middle and end.
# if 0 move start and middle
# if 1 move middle and if 2 then swap with end and reduce end.

def DutchNationFlag(arr):
    start,middle,end = 0,0,len(arr)-1

    while middle<=end:
        if arr[middle]==0:
            arr[start],arr[middle]=arr[middle],arr[start]
            start +=1
            middle +=1
        elif arr[middle]==1:
            middle +=1
        elif arr[middle]==2: 
            arr[middle],arr[end]=arr[end],arr[middle]
            end -=1
    
    return arr

arr =[1,0,2,2,1,1,0,2,2,0,0,1,1]
print(f"The array after sorting will be {DutchNationFlag(arr)}.")