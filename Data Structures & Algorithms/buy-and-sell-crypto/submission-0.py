class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_so_far:
                    max_so_far = prices[j] - prices[i]

        return max_so_far