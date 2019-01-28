class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num==1:
            return True
        l=1
        r=num//2
        while l<=r:
            mid=(l+r)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                r=mid-1
            else:l=mid+1
        return False
