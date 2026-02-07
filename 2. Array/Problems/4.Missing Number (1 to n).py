#Missing Number (1 to n)
#Method 1
def MissingNumber(arr,n):
   total = n*(n+1)//2
   return total-sum(arr)

#Method 2
def MissingNumber2(arr,n):
   res=0
   for i in range(n+1):
      res^=i
   for a in arr:
      res^=a
   return res

arr =[1,4,6,3,5]
print(MissingNumber(arr,6))
print(MissingNumber2(arr,6))
