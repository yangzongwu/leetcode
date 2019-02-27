class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n!=0:
            cur=n&1
            n=n>>1
            if (cur^n)&1!=1:
                return False
        return True
