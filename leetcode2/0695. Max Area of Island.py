class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        if not grid:
            return 0
        rep=0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]==1:
                    res=self.submaxAreaOfIsland(grid,row,column)
                    rep=max(rep,res)
        return rep
    
    def submaxAreaOfIsland(self,grid,row,column):
        rep=1
        grid[row][column]='X'
        if row-1>=0 and grid[row-1][column]==1:
            rep+=self.submaxAreaOfIsland(grid,row-1,column)
        if column-1>=0 and grid[row][column-1]==1:
            rep+=self.submaxAreaOfIsland(grid,row,column-1)
        if row+1<len(grid) and grid[row+1][column]==1:
            rep+=self.submaxAreaOfIsland(grid,row+1,column)
        if column+1<len(grid[0]) and grid[row][column+1]==1:
            rep+=self.submaxAreaOfIsland(grid,row,column+1)
        return rep
        
