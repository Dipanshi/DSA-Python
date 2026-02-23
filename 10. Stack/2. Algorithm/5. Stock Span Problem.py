def calculate_span(prices):
    """
    Calculate span of stock prices
    Time: O(n), Space: O(n)
    """
    stack=[]
    span=[0]*len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]]<=prices[i]:
            stack.pop()
        span[i]=i+1 if not stack else i-stack[-1]
        stack.append(i)
    return span

# Test:
prices = [100, 80, 60, 70, 60, 75, 85]
print(calculate_span(prices))  # [1, 1, 1, 2, 1, 4, 6]