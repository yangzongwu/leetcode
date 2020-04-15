class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_list=set()
        col_list=set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    row_list.add(row)
                    col_list.add(col)
        
        for row in row_list:
            for col in range(len(matrix[0])):
                matrix[row][col]=0
            
        for col in col_list:
            for row in range(len(matrix)):
                matrix[row][col]=0
