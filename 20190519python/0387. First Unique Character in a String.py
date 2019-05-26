class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict={}
        for c in s:
            if c not in s_dict:
                s_dict[c]=1
            else:
                s_dict[c]+=1
        
        for i in range(len(s)):
            if s_dict[s[i]]==1:
                return i
        return -1
