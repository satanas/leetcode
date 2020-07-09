import sys

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        buy_price = sys.maxsize
        sell_price = 0
        
        for price in prices:
            if price < buy_price:
                buy_price = price
                sell_price = price
            elif price > sell_price:
                sell_price = price

            profit = sell_price - buy_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))