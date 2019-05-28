class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w,l=1,area
        lo,hi=w,l
        while lo<=area/lo:
            if lo<=area/lo and area%lo==0:
                w,l=area//lo,lo
            lo+=1
        return [w,l]
