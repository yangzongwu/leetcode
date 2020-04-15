class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        k=0
        while k<len(A):
            A[k]=A[k][::-1]
            i=0
            while i<len(A[k]):
                if A[k][i]==1:
                    A[k][i]=0
                else:
                    A[k][i]=1
                i+=1
            k+=1
        return A
