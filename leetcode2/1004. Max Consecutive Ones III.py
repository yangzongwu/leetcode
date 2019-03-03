class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        st=0
        rep=0
        for i in range(len(A)):
            if A[i]==0 and K>0:
                K-=1
            elif A[i]==0:
                while A[st]==1:
                    st+=1
                st+=1
            rep=max(rep,i-st+1)
        return rep
