'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:flag=-1
        
        x=abs(x)
        s=int(str(x)[::-1])*flag
        if s>2**31-1 or s<-2**31:
            return 0
        else:
            return s
        
############################seconde################################
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=-1
            
        rep=int(str(abs(x))[::-1])*flag
        if rep>2**31-1 or rep<-2**31:
            return 0
        else:
            return rep
        
