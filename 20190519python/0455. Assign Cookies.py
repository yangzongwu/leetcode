class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        rep=0
        i,j=0,0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                rep+=1
                j+=1
            i+=1
        return rep
