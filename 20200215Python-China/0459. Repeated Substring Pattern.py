'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for k in range(len(s)//2):
            if k+1<len(s) and len(s)%(k+1)==0:
                if self.isSubString(s[:k+1],s[k+1:]):
                    return True
        return False

    def isSubString(self,str1,str2):
        if not str2:
            return True
        if str2[:len(str1)]!=str1:
            return False
        return self.isSubString(str1,str2[len(str1):])
