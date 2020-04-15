class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        dp=[0]*30
        for i in range(1,days[-1]+1):
            if i not in days:
                dp.append(dp[i-1+29])
            else:
                dp.append(min(dp[i-1+29]+costs[0],dp[i-7+29]+costs[1],dp[i-30+29]+costs[2]))
        return dp[-1]
