class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        flag1=2**31-1
        flag2=2**32-1
        while b!=0:
            tmp=(a&b)&flag2
            a=(a^b)&flag2
            b=(tmp<<1)&flag2
        if a<flag1:
            return a
        else:
            return ~((flag1&a)^flag1)
