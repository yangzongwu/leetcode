'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        tar = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n<=26:
            return tar[n]
        result = ""
        while n > 0:
            if n % 26:
                m=n%26
                n=n/26
            else:
                m=26
                n=n/26-1
            result=tar[m]+result
        return result
