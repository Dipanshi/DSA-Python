def daily_temperatures(temperatures):
    """
    Find days until warmer temperature
    Time: O(n), Space: O(n)
    """
    stack=[]
    result=[0]*len(temperatures)
    for i,temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]]<temp:
            prev_index=stack.pop()
            result[prev_index]=i-prev_index
        
        stack.append(i)

    return result

# Test:
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temps))  # [1, 1, 4, 2, 1, 1, 0, 0]