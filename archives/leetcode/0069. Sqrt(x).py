'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        if left**2==x:
            return left
        if right**2==x:
            return right
        while left<right-1:
            mid=(left+right)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid
            else:
                right=mid
        return left
