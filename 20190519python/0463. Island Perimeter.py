class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return self.calIslandPerimeter(grid,row,col)
        
    def calIslandPerimeter(self,grid,row,col):
        rep=4
        grid[row][col]=2
        if row-1>=0:
            if grid[row-1][col]==1:
                rep+=self.calIslandPerimeter(grid,row-1,col)-1
            elif grid[row-1][col]==2:
                rep-=1
        if col-1>=0:
            if grid[row][col-1]==1:
                rep+=self.calIslandPerimeter(grid,row,col-1)-1
            elif grid[row][col-1]==2:
                rep-=1
        if row+1<len(grid):
            if grid[row+1][col]==1:
                rep+=self.calIslandPerimeter(grid,row+1,col)-1
            elif grid[row+1][col]==2:
                rep-=1
        if col+1<len(grid[0]):
            if grid[row][col+1]==1:
                rep+=self.calIslandPerimeter(grid,row,col+1)-1
            elif grid[row][col+1]==2:
                rep-=1
        return rep
