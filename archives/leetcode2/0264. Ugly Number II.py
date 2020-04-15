class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        if n==1:
            return 1
        dp=[1]*n
        index2,index3,index5=0,0,0
        for i in range(1,n):
            dp[i]=min(dp[index2]*2,dp[index3]*3,dp[index5]*5)
            if dp[i]==dp[index2]*2:
                index2+=1
            if dp[i]==dp[index3]*3:
                index3+=1
            if dp[i]==dp[index5]*5:
                index5+=1
            
        return dp[n-1]
 #########################################################################################
 class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        from heapq import heappush,heappop
        heap=[1]
        while n>0:
            cur=heappop(heap)
            n-=1
            if cur*2 not in heap:
                heappush(heap,cur*2)
            if cur*3 not in heap:
                heappush(heap,cur*3)
            if cur*5 not in heap:
                heappush(heap,cur*5)
        return cur
