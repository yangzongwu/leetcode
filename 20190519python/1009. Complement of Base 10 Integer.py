class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0:
            return 1
        cur=1
        rep=0
        while N>0:
            if N&1==1:
                cur*=2
                N>>=1
            else:
                rep+=cur
                cur*=2
                N>>=1
        return rep
                
