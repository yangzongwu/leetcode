class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rep=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    rep=max(rep,self.getIsland(grid,row,col))
        return rep
    
    def getIsland(self,grid,row,col):
        rep=1
        grid[row][col]='X'
        if row-1>=0 and grid[row-1][col]==1:
            rep+=self.getIsland(grid,row-1,col)
        if col-1>=0 and grid[row][col-1]==1:
            rep+=self.getIsland(grid,row,col-1)
        if row+1<len(grid) and grid[row+1][col]==1:
            rep+=self.getIsland(grid,row+1,col)
        if col+1<len(grid[0]) and grid[row][col+1]==1:
            rep+=self.getIsland(grid,row,col+1)
        return rep
            
