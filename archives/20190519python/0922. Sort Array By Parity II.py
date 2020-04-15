class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        l=0
        r=len(A)-1
        while l<len(A) and r>0:
            while l<len(A) and A[l]%2==0:
                l+=2
            while r>=0 and A[r]%2!=0:
                r-=2
            if l<len(A):
                A[l],A[r]=A[r],A[l]
                l+=2
                r-=2
        return A
