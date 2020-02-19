'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for k in range(len(haystack)-len(needle)+1):
            if haystack[k]==needle[0] and self.isSameStr(haystack[k:],needle):
                return k
        return -1

    def isSameStr(self,str1,str2):
        for k in range(len(str2)):
            if str2[k]!=str1[k]:
                return False
        return True
    
