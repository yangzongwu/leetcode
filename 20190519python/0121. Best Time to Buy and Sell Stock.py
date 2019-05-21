class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice=prices[0]
        rep=0
        for price in prices:
            minPrice=min(minPrice,price)
            rep=max(rep,price-minPrice)
        return rep
