class Solution:
    def mySqrt(self, x: int) -> int:
        lo=1
        hi=x
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                lo=mid+1
            else:
                hi=mid-1
        return lo-1
