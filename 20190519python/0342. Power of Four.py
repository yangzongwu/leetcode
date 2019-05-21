class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        tmp=0b101010101010101010101010101010101010
        if num&tmp>0:
            return False
        rep=0
        while num>0:
            rep+=num&1
            num>>=1
        return rep==1
        
