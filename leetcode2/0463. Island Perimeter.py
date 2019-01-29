class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]==1:
                    return self.subislandPerimeter(row,column,grid)
        
    def subislandPerimeter(self,row,column,grid):
        rep=4
        grid[row][column]='X'
        if row-1>=0:
            if grid[row-1][column]==1:
                rep+=self.subislandPerimeter(row-1,column,grid)-1
            elif grid[row-1][column]=='X':
                rep-=1
        if column-1>=0:
            if grid[row][column-1]==1:
                rep+=self.subislandPerimeter(row,column-1,grid)-1
            elif grid[row][column-1]=='X':
                rep-=1
        if row+1<len(grid):
            if grid[row+1][column]==1:
                rep+=self.subislandPerimeter(row+1,column,grid)-1
            elif grid[row+1][column]=='X':
                rep-=1
        if column+1<len(grid[0]):
            if grid[row][column+1]==1:
                rep+=self.subislandPerimeter(row,column+1,grid)-1
            elif grid[row][column+1]=='X':
                rep-=1
        return rep
         
