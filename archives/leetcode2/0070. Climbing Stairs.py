class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        rep=[1,1]
        for i in range(1,n):
            rep.append(rep[-1]+rep[-2])
        return rep[-1]
