class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        i=1
        while i<(2**31-1)/3:
            i*=3
        return i%n==0
