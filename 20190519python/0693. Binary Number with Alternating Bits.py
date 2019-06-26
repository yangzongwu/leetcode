class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n>2:
            FN=n&1
            SN=(n&2)>>1
            if FN==SN:
                return False
            n=n>>1
        return True
