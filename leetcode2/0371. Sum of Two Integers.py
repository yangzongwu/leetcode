class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD=0xFFFFFFFF
        MAX_INT=0x7FFFFFFF
        
        while b!=0:
            tmp=((a&b)<<1)&MOD
            a=(a^b)&MOD
            b=tmp&MOD
        if a>=MAX_INT:
            return ~(MAX_INT&a)^MAX_INT
        else:
            return a

        
