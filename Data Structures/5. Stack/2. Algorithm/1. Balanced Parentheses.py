def is_balanced(expression):
    """
    Check if parentheses are balanced
    Time: O(n), Space: O(n)
    """
    stack=[]
    pairs={')':'(','}':'{',']':'['}
    for c in expression:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            if not stack or stack[-1]!=pairs[c]:
                return False
            stack.pop()
    return len(stack)==0
    
# Test:
print(is_balanced("(){}[]"))      # True
print(is_balanced("({[]})"))      # True
print(is_balanced("([)]"))        # False
print(is_balanced("((())"))       # False