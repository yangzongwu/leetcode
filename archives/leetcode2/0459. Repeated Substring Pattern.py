class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:
            return False
        
        for k in range(len(s)):
            flag=s[:k+1]
            tmp=s[k+1:]
            if tmp:
                while tmp[:k+1]==flag:
                    tmp=tmp[k+1:]
                if not tmp:
                    return True
        return False
