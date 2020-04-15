# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo=1
        hi=n
        while lo<=hi:
            mid=(lo+hi)//2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                lo=mid+1
            else:
                hi=mid-1
