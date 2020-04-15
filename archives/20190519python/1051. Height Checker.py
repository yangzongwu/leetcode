class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        tmp=sorted(heights)
        rep=0
        for k in range(len(heights)):
            if heights[k]!=tmp[k]:
                rep+=1
        return rep
