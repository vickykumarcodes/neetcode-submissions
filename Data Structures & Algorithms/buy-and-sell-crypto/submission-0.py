class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
               change = price - min_price
               best = max(best, change)
        return best
    