class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<10:
            if n==7 or n==1:
                return True
            else:
                return False
        rep=0
        while n>0:
            rep+=(n%10)**2
            n=n//10
        return self.isHappy(rep)
