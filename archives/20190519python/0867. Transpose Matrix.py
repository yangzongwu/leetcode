class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rep=[[0]*len(A) for i in range(len(A[0]))]
        for row in range(len(A)):
            for col in range(len(A[0])):
                rep[col][row]=A[row][col]
        return rep
