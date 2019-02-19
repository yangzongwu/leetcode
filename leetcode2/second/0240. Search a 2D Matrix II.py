class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row,column=0,len(matrix[0])-1
        while row<len(matrix) and column>=0:
            if matrix[row][column]>target:
                column-=1
            elif matrix[row][column]<target:
                row+=1
            else:
                return True
        return False
