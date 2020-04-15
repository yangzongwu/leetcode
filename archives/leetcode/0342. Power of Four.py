'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        rep=[]
        while 4**i<2**31-1:
            rep.append(4**i)
            i+=1
        return num in rep
########################################################################
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num>0 and num&(num-1)==0 and num&0b1010101010101010101010101010101==num:
            return True
        return False
