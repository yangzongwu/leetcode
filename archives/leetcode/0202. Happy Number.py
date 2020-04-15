'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those 
numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        else:
            cur=n
            while cur>9:
                n=cur
                cur=0
                while n:
                    cur=cur+(n%10)**2
                    n=(n-n%10)/10
            if cur==7 or cur==1:
                return True
            else:
                return False
