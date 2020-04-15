class Solution:
    def romanToInt(self, s: str) -> int:
        sdict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if not s:
            return 0;
        rep=0
        for i in range(len(s)-1):
            if sdict[s[i]]<sdict[s[i+1]]:
                rep-=sdict[s[i]]
            else:
                rep+=sdict[s[i]]
        rep+=sdict[s[len(s)-1]]
        return rep
