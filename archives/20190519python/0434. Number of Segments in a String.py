class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        rep=0
        s_list=s.split(" ")
        for s in s_list:
            if s:
                rep+=1
        return rep
