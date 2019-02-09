class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        k=0
        while k<len(A):
            A[k]=A[k]**2
            k+=1
        A.sort()
        return A
