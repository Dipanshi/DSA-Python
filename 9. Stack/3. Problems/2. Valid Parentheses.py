def is_valid(s):
    """
    Check if string has valid parentheses
    Time: O(n), Space: O(n)
    """
    stack=[]
    mapping = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in mapping:
            if not stack or stack[-1]!=mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    
    return len(stack)==0

# Test:
print(is_valid("()[]{}"))  # True
print(is_valid("([)]"))    # False