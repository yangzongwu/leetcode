class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix:
            for col in range(1,len(matrix[0])):
                matrix[0][col]+=matrix[0][col-1]
            for row in range(1,len(matrix)):
                matrix[row][0]+=matrix[row-1][0]
            for row in range(1,len(matrix)):
                for col in range(1,len(matrix[0])):
                    matrix[row][col]+=matrix[row-1][col]+matrix[row][col-1]-matrix[row-1][col-1]
        self.matrix=matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.matrix[row2][col2]
        elif row1==0 and col1!=0:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]
        elif row1!=0 and col1==0:
            return self.matrix[row2][col2]-self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2]-self.matrix[row2][col1-1]-self.matrix[row1-1][col2]+self.matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
