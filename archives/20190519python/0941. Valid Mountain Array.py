class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        
        cur=0
        for k in range(len(A)-1):
            if A[k]==A[k+1]:
                return False
            if A[k]>A[k+1]:
                cur=k
                break
        if cur==0:
            return False
        for k in range(cur,len(A)-1):
            if A[k]==A[k+1]:
                return False
            if A[k]<A[k+1]:
                return False
        return True
