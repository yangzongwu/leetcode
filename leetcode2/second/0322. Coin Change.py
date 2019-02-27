class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        coins.sort()
        if amount==0:
            return 0
        if amount<coins[0]:
            return -1
        dp=[]
        for k in range(amount+1):
            if k<coins[0]:
                dp.append(-1)
            elif k in coins:
                dp.append(1)
            else:
                cur=amount+1
                for coin in coins:
                    if k-coin>0 and dp[k-coin]!=-1:
                        cur=min(cur,dp[k-coin]+1)
                if cur==amount+1:
                    cur=-1
                dp.append(cur)
        return dp[-1]
                        
        
