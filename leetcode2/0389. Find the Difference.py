class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicts={}
        for ss in s:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        for tt in t:
            if tt not in dicts:
                return tt
            if dicts[tt]==0:
                return tt
            dicts[tt]-=1
