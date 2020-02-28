'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if l==r+1:
                    return True
                if (s[l]==s[r-1] and self.isPalindrom(s[l:r])) or (s[l+1]==s[r] and self.isPalindrom(s[l+1:r+1])):
                    return True
                else:
                    return False
        return True

    def isPalindrom(self,s):
        return s==s[::-1]
