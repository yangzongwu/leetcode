class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:return 1
        if n<0:x,n=1/x,-n
        flag=1
        if x<0 and n%2!=0:flag=-1
        if x<0:x=abs(x)
        
        
        rep=1
        while n>1:
            cur=x
            i=1
            while 2*i<=n:
                i=i+i
                cur=cur*cur
            rep=rep*cur
            n=n-i
        if n==1:rep= rep*x
        if flag==-1:rep=-rep
        if rep>2**32-1:return 2**31-1
        if rep<-2**31:return -2**31
        return rep
