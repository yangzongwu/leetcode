'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i=0
        dicts={}
        for strs in ss:
            dicts[strs]=i+1
            i+=1
        lens=len(s)-1
        rep=0
        for strs in s:
            rep+=26**lens*dicts[strs]
            lens-=1
        return rep
