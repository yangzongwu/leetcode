class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        for row in range(0,n//2+1):
            for column in range(row,n-row):
                matrix[row][column], matrix[column][n-row],matrix[n-row][n-column],matrix[n-column][row]=
                matrix[n-column][row],matrix[row][column], matrix[column][n-row],matrix[n-row][n-column]
