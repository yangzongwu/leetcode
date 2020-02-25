'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c ** 0.5)
        while left<=right:
            if left**2+right**2==c:
                return True
            elif left**2+right**2>c:
                right-=1
            else:
                left+=1
        return False
