class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost)
        if len(cost)<2:
            return 0
        
        dp=[]
        dp.append(cost[0])
        dp.append(cost[1])
        
        for i in range(2,len(cost)):
            dp.append(cost[i]+min(dp[-1],dp[-2]))
        return min(dp[-1],dp[-2])
