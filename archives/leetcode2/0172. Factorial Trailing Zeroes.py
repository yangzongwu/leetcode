class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        rep=0
        if n<5:return 0
        
        while n>=5:
            n=n//5
            rep+=n
            
        return rep
