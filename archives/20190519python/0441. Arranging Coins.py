class Solution:
    def arrangeCoins(self, n: int) -> int:
        #(1+i)*i//2
        lo=0
        hi=n
        while lo<=hi:
            mid=lo+(hi-lo)//2
            target=(1+mid)*mid//2
            if target==n:
                return mid
            elif target>n:
                hi=mid-1
            else:
                lo=mid+1
        return lo-1
