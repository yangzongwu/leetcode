class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s)==1:
            return 1
        
        left=0
        right=left+1
        rep=0
        while right<len(s):
            if s[right] not in s[left:right]:
                right+=1
            else:
                rep=max(rep,right-left)
                while s[left]!=s[right]:
                    left+=1
                left+=1
                right+=1
        rep=max(rep,right-left)
        return rep
