class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        s_dict={}
        for c in s:
            if c not in s_dict:
                s_dict[c]=1
            else:
                s_dict[c]+=1
        rep=0
        for k in s_dict:
            rep+=s_dict[k]//2
            
        if rep*2==len(s):
            return rep*2
        return rep*2+1
        
