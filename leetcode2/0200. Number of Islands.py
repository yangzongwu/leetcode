class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        cnt=0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]=='1':
                    self.subnumIslands(grid,row,column)
                    cnt+=1
        return cnt
    
    def subnumIslands(self,grid,row,column):
        grid[row][column]='X'
        if row-1>=0 and grid[row-1][column]=='1':
            self.subnumIslands(grid,row-1,column)
        if column-1>=0 and grid[row][column-1]=='1':
            self.subnumIslands(grid,row,column-1)
        if row+1<len(grid) and grid[row+1][column]=='1':
            self.subnumIslands(grid,row+1,column)
        if column+1<len(grid[0]) and grid[row][column+1]=='1':
            self.subnumIslands(grid,row,column+1)
        
