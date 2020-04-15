class Solution:
    def rotatedDigits(self, N: int) -> int:
        rep=0
        for i in range(2,N+1):
            if self.isGoodDigit(i):
                rep+=1
        return rep

    def isGoodDigit(self,N):
        res=str(N)
        for s in "347":
            if s in res:
                return False
        for s in "2569":
            if s in res:
                return True
        return False
