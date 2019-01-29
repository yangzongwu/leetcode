class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ks,kg=0,0
        rep=0
        while ks<len(s) and kg<len(g):
            if s[ks]>=g[kg]:
                rep+=1
                ks+=1
                kg+=1
            else:
                ks+=1
        return rep
