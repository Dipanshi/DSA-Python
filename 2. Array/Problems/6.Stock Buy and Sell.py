#Stock Buy and Sell (One Transaction)
# You are given:
# An array/list of stock prices
# Each price represents the stock price on a particular day
# You are allowed to make only ONE transaction  Prices = [7, 1, 5, 3, 6, 4]

def StockBuySell(arr):
    buy_price=float('inf')
    max_profit=0
    for a in arr:
        buy_price=min(buy_price,a)
        max_profit=max(max_profit,a-buy_price)
    return max_profit

Prices = [7, 5, 3, 6,1, 4]
print(StockBuySell(Prices))
