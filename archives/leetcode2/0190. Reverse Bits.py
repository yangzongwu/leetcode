class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n==0:
            return 0
        res=0
        for _ in range(32):
            res=res<<1
            res=res+(n&1)
            n=n>>1    
        return res
