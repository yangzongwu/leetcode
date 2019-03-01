class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.dp=[[0 for column in range(len(matrix[0]))] for row in range(len(matrix))]    
        self.dp[0][0]=matrix[0][0]
        for row in range(1,len(matrix)):
            self.dp[row][0]=self.dp[row-1][0]+matrix[row][0]
            
        for column in range(1,len(matrix[0])):
            self.dp[0][column]=self.dp[0][column-1]+matrix[0][column]
                
        for row in range(1,len(matrix)):
            for column in range(1,len(matrix[0])):
                self.dp[row][column]=matrix[row][column]+self.dp[row-1][column]+self.dp[row][column-1]-self.dp[row-1][column-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.dp[row2][col2]
        elif row1!=0 and col1!=0:
            return self.dp[row2][col2]+self.dp[row1-1][col1-1]-self.dp[row2][col1-1]-self.dp[row1-1][col2]
        elif row1==0 and col1!=0:
            return self.dp[row2][col2]-self.dp[row2][col1-1]
        else:
            return self.dp[row2][col2]-self.dp[row1-1][col2]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
