class Solution:
    def reverseVowels(self, s: str) -> str:
        sList=list(s)
        lo=0
        hi=len(s)-1
        target='aoiueAOUIE'
        while lo<hi:
            while lo<hi and sList[lo] not in target:
                lo+=1
            while hi>lo and sList[hi] not in target:
                hi-=1
            if lo<hi:
                sList[lo],sList[hi]=sList[hi],sList[lo]
                lo+=1
                hi-=1
        return "".join(sList)
