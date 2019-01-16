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
#####################Memory Limit Exceeded
#####################Time Limit Exceeded
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        max_len=0
        rep=''
        for k in range(len(s)):
            k_len=self.preLongestPalindrome(s[k:])[0]
            k_rep=self.preLongestPalindrome(s[k:])[1]
            if k_len>max_len:
                max_len=k_len
                rep=k_rep
        return rep
    
    def preLongestPalindrome(self,s):
        for k in range(len(s),-1,-1):
            if s[:k]==s[:k][::-1]:
                return [k,s[:k]]
####################################
 class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        max_len = 0
        rep = ''
        for k in range(len(s)):
            k_rep = self.preLongestPalindrome(s, k)
            if len(k_rep) > max_len:
                max_len = len(k_rep)
                rep = k_rep
        return rep

    def preLongestPalindrome(self, s, k):
        gap = 0
        rep=s[k]
        rep1,rep2='',''
        while k - gap >= 0 and k + gap < len(s):
            if s[k - gap] == s[k + gap]:
                rep1 = s[k - gap:k + gap + 1]
                gap += 1
            else:
                break
        if k + 1 < len(s) and s[k] == s[k + 1]:
            gap = 0
            while k - gap >= 0 and k + 1 + gap < len(s):
                if s[k - gap] == s[k + 1 + gap]:
                    rep2 = s[k - gap:k + 1 + gap + 1]
                    gap += 1
                else:
                    break
        if len(rep2) > len(rep1):
            return rep2
        else:
            return rep1
