class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        if len(s)>1:
            l=0
            r=len(s)-1
            while r>=l+1:
                s[r],s[l]=s[l],s[r]
                r-=1
                l+=1
