class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> 'bool':
        row=len(matrix)-1
        column=0
        while row>=0 and column<len(matrix[0]):
            if not self.subisToeplitzMatrix(row,column,matrix):
                return False
            else:
                if row!=0:
                    row-=1
                else:
                    column+=1
        return True
    
    def subisToeplitzMatrix(self,row,column,matrix):
        target=matrix[row][column]
        while row+1<len(matrix) and column+1<len(matrix[0]):
            if matrix[row+1][column+1]!=target:
                return False
            else:
                row+=1
                column+=1
        return True
