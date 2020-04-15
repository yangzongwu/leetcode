class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if amount==0:
            return 0
        coins.sort()
        dp=[-1]
        for k in range(1,amount+1):
            if k<coins[0]:
                dp.append(-1)
            elif k in coins:
                dp.append(1)
            else:
                cur=amount+1
                for coin in coins:
                    if k-coin>=0 and dp[k-coin]!=-1:
                        cur=min(cur,1+dp[k-coin])
                if cur==amount+1:
                    cur=-1
                dp.append(cur)
        return dp[-1]
                
