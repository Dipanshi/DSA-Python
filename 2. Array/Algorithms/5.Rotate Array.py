#Rotate Array left or right.
"""Rotate array k steps to the right - O(n)"""
def RotateRight(arr,k):
  n=len(arr)
  k=k%n
  return arr[-k:]+arr[:-k]

"""Rotate array k steps to the left - O(n)"""
def RotateLeft(arr,k):
  n=len(arr)
  k=k%n
  return arr[k:]+arr[:k] 

# In-place rotation using reversal
def reverse1(arr,start,end):
  while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start +=1
    end-=1

def InplaceRotation(arr,k):
  n=len(arr)
  k=k%n
  reverse1(arr,0,n-1)    #reverse full arr
  reverse1(arr,0,k-1)    #reverse first half
  reverse1(arr,k,n-1)    #reverse second half
  return arr


arr=[12,3,5,2,6,8,9,11]
print(arr)
print(InplaceRotation(arr,2))
print(RotateLeft(arr,3))
print(RotateRight(arr,4))
