class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n<=2:
            return 1
        l=1
        r=n
        while r>=l:
            mid=(r+l)//2
            flag=self.calArrangeMidCoin(mid)
            if flag==n:
                return mid
            elif flag>n:
                r=mid-1
            else:
                l=mid+1
        return r
                
            
    def calArrangeMidCoin(self,n):
        return (1+n)*n/2
