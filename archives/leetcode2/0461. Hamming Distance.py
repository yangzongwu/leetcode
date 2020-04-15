class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        rep=0
        for _ in range(32):
            if (x&1)^(y&1)==1:
                rep+=1
            x=x>>1
            y=y>>1
        return rep
