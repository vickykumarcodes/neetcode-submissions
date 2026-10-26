class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        first we check through each element of the list from 2nd element i.e-           prices[1] to len(prices)
        then we can calculate the chage if change is positive, add change to profit
        """
        profit = 0

        for i in range(1, len(prices)):
            change = prices[i] - prices[i -1]
            if change > 0:
                profit += change

        return profit