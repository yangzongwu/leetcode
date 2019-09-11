class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r and s[l]==s[r]:
            l+=1
            r-=1
        if l>=r:
            return True
        return self.isValidPalindrome(s[l:r]) or self.isValidPalindrome(s[l+1:r+1])
    
    def isValidPalindrome(self,s):
        return s==s[::-1]
