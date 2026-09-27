class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        min_so_far = prices[0]
        for i in range(len(prices)):
            # consider index i to be the buying price
            if min_so_far > prices[i]:
                min_so_far = prices[i]
            profit = prices[i] - min_so_far
            if max_so_far < profit:
                max_so_far = profit

        return max_so_far