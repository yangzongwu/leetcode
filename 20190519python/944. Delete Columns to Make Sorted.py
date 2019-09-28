class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A)<1:
            return 0
        
        cnt=0
        for i in range(len(A[0])):      
            k=1
            while k<len(A):
                if A[k-1][i]>A[k][i]:
                    break
                k+=1
            if k<len(A):
                cnt+=1
                
        return cnt
