class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        
        rep=0
        for k in range(len(A)):
            rep+=k*A[k]
        
        sumOfA=sum(A)
        lenOfA=len(A)
        cur=rep
        
        for i in range(len(A)-1,0,-1):
            cur=cur+sumOfA-lenOfA*A[i]
            rep=max(rep,cur)
        return rep
