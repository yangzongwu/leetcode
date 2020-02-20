'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        if s[-1]==" ":
            return self.lengthOfLastWord(s[:-1])
        
        return self.getLengthOfLastWord(s,0)

    def getLengthOfLastWord(self,s,n):
        if not s:
            return n
        if s[-1]==" ":
            return n
        return self.getLengthOfLastWord(s[:-1],n+1)
