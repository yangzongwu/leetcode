class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        rep=0
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]=='1':
                    rep=max(rep,self.submaximalSquare(row,column,matrix))
        return rep*rep
    
    def submaximalSquare(self,row,column,matrix):
        rep=1
        for i in range(1,len(matrix)):
            if row+i==len(matrix) or column+i==len(matrix[0]):
                return rep
            else:
                for k in range(i+1):
                    if matrix[row+k][column+i]!='1' or matrix[row+i][column+k]!='1':
                        return rep
                rep+=1
        return rep
