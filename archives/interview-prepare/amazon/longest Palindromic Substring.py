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
        if not s or len(s)==1:
            return s
        rep,res=0,''
        for k in range(len(s)-1):
            cur=self.single_longestPalindrome(k,s)
            if cur[0]>rep:
                rep=cur[0]
                res=cur[1]
            if s[k+1]==s[k]:
                cur=self.double_longestPalindrome(k,s)
                if cur[0]>rep:
                    rep=cur[0]
                    res=cur[1]
        return res
    
    def single_longestPalindrome(self,k,s):
        i=1
        while k-i>=0 and k+i<len(s) and s[k-i]==s[k+i]:
            i+=1
        i-=1 
        return [2*i+1,s[k-i:k+i+1]]
    
    def double_longestPalindrome(self,k,s):
        i=1
        while k-i>=0 and k+1+i<len(s) and s[k-i]==s[k+1+i]:
            i+=1
        i-=1
        return [2*i+2,s[k-i:k+1+i+1]]
