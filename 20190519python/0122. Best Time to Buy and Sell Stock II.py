class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rep=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                rep+=prices[i+1]-prices[i]
        return rep
