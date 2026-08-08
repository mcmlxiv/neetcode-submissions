class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]

        for p in prices:
            buy = min(buy, p)
            profit = p - buy

            maxP = max(profit, maxP)
        
        return maxP

