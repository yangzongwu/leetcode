'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        if num==0 or num==1:
            return True
        left=0
        right=num//2
        while right>=left:
            mid=(left+right)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                right=mid-1
            else:
                left=mid+1
        return False
