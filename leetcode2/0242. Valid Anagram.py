class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dictst={}
        for ss  in s:
            if ss not in dictst:
                dictst[ss]=1
            else:
                dictst[ss]+=1
        for tt in t:
            if tt not in dictst:
                return False
            else:
                dictst[tt]-=1
        for key in dictst:
            if dictst[key]!=0:
                return False
        return True
