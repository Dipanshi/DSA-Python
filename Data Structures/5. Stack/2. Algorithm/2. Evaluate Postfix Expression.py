def evaluate_postfix(expression):
    """
    Evaluate postfix expression
    Time: O(n), Space: O(n)
    """
    stack=[]
    for c in expression.split():
        if c.isdigit() or (c[0]=="-" and c[1:].isdigit()):
            stack.append(int(c))
        else:
            num2=stack.pop()
            num1=stack.pop()
            if c=="+":
                stack.append(num1+num2)
            elif c=="-":
                stack.append(num1-num2)
            elif c=="*":
                stack.append(num1*num2)
            elif c=="/":
                stack.append(int(num1/num2))

    return stack[0]
    
# Test:
print(evaluate_postfix("2 3 + 5 *"))  # (2+3)*5 = 25
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))  # 5+((1+2)*4)-3 = 14