class Solution:
    def clumsy(self, N: int) -> int:
        def subclumns(N):
            if N==0:
                return 0
            if N==1:
                return 1
            if N==2:
                return 2
            if N==3:
                return 6
        if N<4:
            return subclumns(N)
        rep=N*(N-1)//(N-2)+(N-3)
        N-=4
        while N>=4:
            rep=rep-N*(N-1)//(N-2)+(N-3)
            N-=4
        return rep-subclumns(N)
        
