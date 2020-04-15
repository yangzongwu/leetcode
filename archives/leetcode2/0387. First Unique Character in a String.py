class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={}
        for ss in s:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        for k in range(len(s)):
            if dicts[s[k]]==1:
                return k
        return -1
