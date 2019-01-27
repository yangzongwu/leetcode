class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(s):
            return False
        if not s:
            return True
        dictst={}
        listt=set()
        for k in range(len(s)):
            if s[k] not in dictst:
                if t[k] not in listt:
                    dictst[s[k]]=t[k]
                    listt.add(t[k])
                else:
                    return False
            else:
                if dictst[s[k]]!=t[k]:
                    return False
        return True
