class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        lo=0
        hi=num
        while lo<=hi:
            mid=(lo+hi)//2
            if mid**2==num:
                return True
            elif mid**2<num:
                lo=mid+1
            else:
                hi=mid-1
        return False
