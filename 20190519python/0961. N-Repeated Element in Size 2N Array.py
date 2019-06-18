class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        FN=A[len(A)//2-1]
        SN=A[len(A)//2]
        if FN==SN:
            return FN
        if A[0]==FN:
            return FN
        else:
            return SN
