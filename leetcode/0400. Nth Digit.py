'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        digit=1#位数
        while n>digit*9*10**(digit-1):
            n-=digit*9*10**(digit-1)
            digit+=1
        
        num=10**(digit-1)+(n-1)//digit
        b=(n-1)%digit
        return int(str(num)[b])
    
