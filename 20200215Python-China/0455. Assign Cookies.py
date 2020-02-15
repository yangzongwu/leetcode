class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt=0
        gk,sk=0,0
        while gk<len(g) and sk<len(s):
            if s[sk]>=g[gk]:
                sk+=1
                gk+=1
                cnt+=1
            else:
                sk+=1
        return cnt
