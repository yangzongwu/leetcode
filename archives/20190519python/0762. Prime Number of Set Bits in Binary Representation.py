class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        rep=0
        for num in range(L,R+1):
            cnt=self.count1(num)
            if self.isPrime(cnt):
                rep+=1
        return rep

    def count1(self,num):
        rep=0
        while num>0:
            rep+=num&1
            num>>=1
        return rep

    def isPrime(self,num):
        rep=(2,3,5,7,11,13,17,19,23,29,31)
        if num in rep:
            return True
        return False
