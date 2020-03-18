'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        rep=""
        for k in range(len(s)):
            if k+1<len(s) and s[k]==s[k+1]:
                str1=self.isPalindrome(s,k,k)
                str2=self.isPalindrome(s,k,k+1)
                if len(str1)>len(rep):
                    rep=str1
                if len(str2)>len(rep):
                    rep=str2
            else:
                str1=self.isPalindrome(s,k,k)
                if len(str1)>len(rep):
                    rep=str1
        return rep

    def isPalindrome(self,s,l,r):
        while l-1>=0 and r+1<len(s) and s[l-1]==s[r+1]:
            l-=1
            r+=1
        return s[l:r+1]

