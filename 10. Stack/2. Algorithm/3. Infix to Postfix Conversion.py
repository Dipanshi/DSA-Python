def infix_to_postfix(expression):
    """
    Convert infix to postfix
    Time: O(n), Space: O(n)
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Test:
print(infix_to_postfix("A+B*C"))      # ABC*+
print(infix_to_postfix("(A+B)*C"))    # AB+C*