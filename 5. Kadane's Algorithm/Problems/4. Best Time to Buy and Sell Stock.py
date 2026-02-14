    # Maximum profit with one transaction
    # Similar to max subarray of price differences
    # Time: O(n), Space: O(1)

def max_profit(prices):
    if not prices:
        return 0
    min_price=prices[0]
    max_profit=0
    for price in prices:
        max_profit= max(max_profit,price-min_price)
        min_price= min(price,min_price)
    
    return max_profit

# Using Kadane's approach on differences
def max_profit_kadane(prices):
    """Using Kadane on price differences"""
    if len(prices) < 2:
        return 0
    
    max_current = max_global = 0
    
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        max_current = max(0, max_current + diff)
        max_global = max(max_global, max_current)
    
    return max_global

print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit_kadane([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit_kadane([7, 6, 4, 3, 1]))     # 0