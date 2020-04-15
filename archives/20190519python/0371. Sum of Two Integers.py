class Solution:
    def getSum(self, a: int, b: int) -> int:
        MOD=0XFFFFFFFF
        MAX_INT=0X7FFFFFFF
        
        while b!=0:
            cur=(a&b)&MOD
            a=(a^b)&MOD
            b=(cur<<1)&MOD
        
        if a<MAX_INT:
            return a
        else:
            return ~(a&MAX_INT)^MAX_INT
        
        
