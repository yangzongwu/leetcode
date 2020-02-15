class Solution:
    def romanToInt(self, s: str) -> int:
        dict_s={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if not s:
            return 0
        rep=dict_s[s[-1]]
        for k in range(len(s)-1):
            if dict_s[s[k]]<dict_s[s[k+1]]:
                rep-=dict_s[s[k]]
            else:
                rep+=dict_s[s[k]]
        return rep
