class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rep=0
        for i in range(32):
            cur=n&1
            rep<<=1
            rep|=cur
            n>>=1
        return rep
