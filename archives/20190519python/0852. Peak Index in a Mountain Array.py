class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        k=1
        while k<len(A) and A[k]>A[k-1]:
            k+=1
        return k-1
