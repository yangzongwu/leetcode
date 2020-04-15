class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=-1
        x=abs(x)
        
        n=0
        while x>0:
            n=n*10+x%10
            x//=10
        
        if flag==-1:
            n=-n
        
        if n>2**31-1 or n<-2**31:
            return 0
        return n
