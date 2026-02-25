def largest_rectangle_area(heights):
    """
    Find largest rectangle in histogram
    Time: O(n), Space: O(n)
    """
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area

# Test:
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # 10