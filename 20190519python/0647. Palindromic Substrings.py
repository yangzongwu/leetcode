class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        rep=0
        for k in range(len(s)):
            rep+=self.countSubstringsFromK(s,k-1,k+1)
            if k+1<len(s) and s[k]==s[k+1]:
                rep+=self.countSubstringsFromK(s,k-1,k+2)
        return rep
    
    def countSubstringsFromK(self,s,l,r):
        rep=1
        while l>=0 and r<len(s) and s[l]==s[r]:
            rep+=1
            l-=1
            r+=1
        return rep
    
