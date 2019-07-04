class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cur_len=len(matrix)-1
        for row in range(0,len(matrix)//2):
            for col in range(row,len(matrix)-row-1):
                matrix[row][col],matrix[col][cur_len-row],
                matrix[cur_len-row][cur_len-col],matrix[cur_len-col][row]=
                matrix[cur_len-col][row],matrix[row][col],
                matrix[col][cur_len-row],matrix[cur_len-row][cur_len-col]
