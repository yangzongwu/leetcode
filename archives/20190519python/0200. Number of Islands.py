class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rep=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    rep+=1
                    self.refillLands(row,col,grid)
        return rep
    
    def refillLands(self,row,col,grid):
        grid[row][col]='0'
        if row-1>=0 and grid[row-1][col]=='1':
            self.refillLands(row-1,col,grid)
        if col-1>=0 and grid[row][col-1]=='1':
            self.refillLands(row,col-1,grid)
        if row+1<len(grid) and grid[row+1][col]=='1':
            self.refillLands(row+1,col,grid)
        if col+1<len(grid[0]) and grid[row][col+1]=='1':
            self.refillLands(row,col+1,grid)
