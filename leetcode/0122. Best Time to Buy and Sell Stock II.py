'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        rep=0
        left,right=0,1
        while right<len(prices):
            if prices[right]<prices[left]:
                left=right
            else:
                while right+1<len(prices) and prices[right+1]>prices[right]:
                    right+=1
                if right+1==len(prices):
                    rep+=prices[right]-prices[left]
                    return rep
                else:
                    rep+=prices[right]-prices[left]
                    left=right+1
                    right=left+1
        return rep
 ###############################################################
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        firstbuy=0
        while firstbuy<len(prices)-1:
            if prices[firstbuy]>prices[firstbuy+1]:
                firstbuy+=1
            else:
                break
        lastsell=len(prices)-1
        while lastsell>0:
            if prices[lastsell]<prices[lastsell-1]:
                lastsell-=1
            else:
                break
        if firstbuy>=lastsell:
            return 0
        else:
            return self.submaxprofit(prices[firstbuy:lastsell+1])
        
    def submaxprofit(self,prices):
        i=0
        rep=0
        while i<len(prices)-1:
            if prices[i+1]>prices[i]:
                rep+=prices[i+1]-prices[i]
            i+=1  
        return rep
                    
