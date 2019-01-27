class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        
        rep=3**10
        while rep<2**31-1:
            rep=rep*3
        rep=rep//3
        
        return rep%n==0
