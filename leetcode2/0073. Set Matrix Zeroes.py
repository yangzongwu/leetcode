class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]==0:
                    self.fill_x_matrix(matrix,row,column)
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]=='X':
                    matrix[row][column]=0
        
    def fill_x_matrix(self,matrix,row,column):
        matrix[row][column]='X'
        for row1 in range(len(matrix)):
            if matrix[row1][column]!=0 and matrix[row1][column]!='X':
                matrix[row1][column]='X'
        for column1 in range(len(matrix[0])):
            if matrix[row][column1]!=0 and matrix[row][column1]!='X':
                matrix[row][column1]='X'
                
