class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        cnta=0
        cntb=0
        for a in A:
            if a>=0:
                cnta+=1
            else:
                cntb+=1
        
        if K<=cntb:
            return -sum(A[:K])+sum(A[K:])
        elif K>cntb:
            K-=cntb
            rep=sum(abs(x) for x in A)
            min_a=min(abs(x) for x in A)
            if K%2==0:
                return rep
            else:
                return rep-2*min_a
