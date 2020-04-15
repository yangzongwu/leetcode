class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for k in range(len(A)):
                A[k].reverse()
                for i in range(len(A[k])):
                    A[k][i]^=1
        return A
    
