class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo=0
        hi=len(s)-1
        while lo<hi:
            s[lo],s[hi]=s[hi],s[lo]
            lo+=1
            hi-=1
