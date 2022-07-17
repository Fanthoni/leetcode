from typing import List


class Solution:
    # Time limit exceeded
    def maxProfit(self, prices: List[int]) -> int:
        # currBestProfit = 0
        # for i in range(len(prices) - 1):
        #     highestSellPrice = max(prices[i+1::])
        #     profitFromToday = highestSellPrice - prices[i]

        #     currBestProfit = profitFromToday if profitFromToday > currBestProfit else currBestProfit
        # return currBestProfit

        if len(prices) <= 1:
            return 0
        maxProfit, minPrice = float("-inf"), prices[0]
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit
