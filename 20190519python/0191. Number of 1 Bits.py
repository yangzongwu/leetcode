class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rep=0
        while n>0:
            rep+=n&1
            n>>=1
        return rep
