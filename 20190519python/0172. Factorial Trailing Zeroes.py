class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        rep=0
        while n>=5:
            rep+=n//5
            n//=5
        return rep
