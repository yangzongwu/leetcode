# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if isBadVersion(mid)==False:
                lo=mid+1
            else:
                hi=mid-1
        return lo
