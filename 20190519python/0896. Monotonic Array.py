class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A)<=1:
            return True
        if A[0]<A[1]:
            for i in range(1,len(A)):
                if A[i-1]>A[i]:
                    return False
        elif A[0]>A[1]:
            for i in range(1,len(A)):
                if A[i-1]<A[i]:
                    return False
        else:
            return self.isMonotonic(A[1:])
        return True
