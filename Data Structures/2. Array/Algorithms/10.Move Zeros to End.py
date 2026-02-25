# Algo to move Zeros to the end.
#Method1
def MoveZero(arr):
    start,end=0,len(arr)-1
    while start<end:
        if arr[start]==0:
            arr[start],arr[end]=arr[end],arr[start]
            end -=1
        else:
            start +=1
    return arr
#Method2
def MoveZero2(arr):
    no_zero_pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[no_zero_pos],arr[i]=arr[i],arr[no_zero_pos]
            no_zero_pos+=1
    return arr

arr =[1,0,3,4,0,0,3,0,9,0,0]
print(MoveZero(arr))
print(MoveZero2(arr))