class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        k=0
        for tt in t:
            if tt==s[k]:
                k+=1
                if k==len(s):
                    return True
        return False
