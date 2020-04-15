class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        listn=[0]*n
        listn[0]=1
        listn[1]=1
        for i in range(2,n//2+1):
            if listn[i]==0:
                k=2
                while i*k<n:
                    listn[i*k]=1
                    k+=1
        rep=0
        for num in listn:
            if num==0:
                rep+=1
        return rep
