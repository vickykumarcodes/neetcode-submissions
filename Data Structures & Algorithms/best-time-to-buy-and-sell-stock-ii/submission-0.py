class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            if change > 0:
                profit += change
        return profit