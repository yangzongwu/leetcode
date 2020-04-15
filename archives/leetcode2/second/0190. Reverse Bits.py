class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rep=0
        for _ in range(32):
            tmp=1&n
            rep=(rep<<1)+tmp
            
            n=n>>1
        return rep
