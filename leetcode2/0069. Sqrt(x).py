class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:return 0
        if x==1:return 1
        
        l=0
        r=x//2
        while r>=l:
            mid=(r+l)//2
            if mid**2==x:
                return mid
            elif mid**2>x:
                r=mid-1
            else:
                l=mid+1
        return r
    
    
    
