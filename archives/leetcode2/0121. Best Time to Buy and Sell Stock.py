class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low=prices[0]
        high=prices[0]
        rep=0
        for price in prices:
            if price<=low:
                low=price
                high=price
            else:
                high=price
                rep=max(rep,high-low)
        return rep
