class Solution:
    def findComplement(self, num: int) -> int:
        rep=0
        cnt=0
        while num>0:
            flag=(num&1)^1
            rep+=flag<<cnt
            cnt+=1
            num>>=1
        return rep
