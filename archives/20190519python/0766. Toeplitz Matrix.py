class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(0,len(matrix)):
            if self.IsNotToeplitzMatrix(matrix,row,0):
                return False
        for col in range(1,len(matrix[0])):
            if self.IsNotToeplitzMatrix(matrix,0,col):
                return False
        return True
    
    def IsNotToeplitzMatrix(self,matrix,row,col):
        target=matrix[row][col]
        while row<len(matrix) and col<len(matrix[0]):
            if matrix[row][col]!=target:
                return True
            row+=1
            col+=1
        return False
