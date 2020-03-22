'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    cnt+=1
                    self.reFilIsland(grid,row,col)
        return cnt


    def reFilIsland(self,grid,row,col):
        grid[row][col]='0'
        if row-1>=0 and grid[row-1][col]=='1':
            self.reFilIsland(grid,row-1,col)
        if col-1>=0 and grid[row][col-1]=='1':
            self.reFilIsland(grid,row,col-1)
        if row+1<len(grid) and grid[row+1][col]=='1':
            self.reFilIsland(grid,row+1,col)
        if col+1<len(grid[0]) and grid[row][col+1]=='1':
            self.reFilIsland(grid,row,col+1) 
