class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        for _ in range(16):
            if num==1:
                return True
            if num&3!=0:
                return False
            num=num>>2
        return True
