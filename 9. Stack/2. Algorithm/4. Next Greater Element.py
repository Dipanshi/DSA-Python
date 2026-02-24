def next_greater_element(arr):
    """
    Find next greater element for each element
    Time: O(n), Space: O(n)
    """
    stack=[]
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        if stack and stack[-1]<arr[i]:
            stack.pop()
        if stack:
            result[i]=stack[-1]
        stack.append(arr[i])

    return result

# Test:
print(next_greater_element([4, 5, 2, 10, 8]))
# [5, 10, 10, -1, -1]