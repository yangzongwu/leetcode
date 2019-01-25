class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rep=0
        for k in range(0,len(prices)-1):
            if prices[k+1]>prices[k]:
                rep+=prices[k+1]-prices[k]
        return rep
