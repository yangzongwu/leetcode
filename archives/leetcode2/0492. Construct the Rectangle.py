import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area==0:
            return [0,0]

        L=math.sqrt(area)
        if area%L==0:
            return [int(L),int(L)]
        L=int(L)
        L=area//L
        while area%L!=0:
            L+=1
        return [L,area//L]
