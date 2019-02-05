class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        rep=0
        if x>=0 and n>=0:
            rep=self.submyPow(x,n)
        elif x>=0 and n<0:
            rep=1/self.submyPow(x,-n)
        elif x<0 and n%2==0 and n>=0:
            rep=self.submyPow(-x,n)
        elif x<0 and n%2==0 and n<0:
            rep=1/self.submyPow(-x,n)
        elif x<0 and n%2!=0 and n>0:
            rep=-self.submyPow(-x,n)
        else:
            rep=-1/self.submyPow(-x,n)
        return rep
    
    def submyPow(self,x,n):
        rep=1
        while n>0:
            cur=x
            cnt=1
            while cnt*2<n:
                cur=cur*cur
                cnt=cnt+cnt
            n=n-cnt
            rep*=cur
        return rep
