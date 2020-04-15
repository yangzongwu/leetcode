class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dist_st={}
        used_word=set()
        for i in range(len(s)):
            if s[i] not in dist_st:
                if t[i] in used_word:
                    return False
                dist_st[s[i]]=t[i]
                used_word.add(t[i])
            else:
                if dist_st[s[i]]!=t[i]:
                    return False
        return True
