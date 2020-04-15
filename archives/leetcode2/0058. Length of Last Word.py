class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        right=len(s)-1
        while right>=0 and s[right]==' ':
            right-=1
        if right==-1:return 0
        
        k=right
        while k>=0:
            if s[k]==' ':
                break
            else:
                k-=1
        return right-k
