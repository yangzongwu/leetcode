'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded 
by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four 
edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_of_island=0
        for line in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[line][column]=='1':
                    num_of_island+=1
                    self.remarkIslands(grid,line,column)
        return num_of_island
    
    def remarkIslands(self,grid,line,column):
        grid[line][column]='X'
        if line-1>=0 and grid[line-1][column]=='1':
            self.remarkIslands(grid,line-1,column)
        if column-1>=0 and grid[line][column-1]=='1':
            self.remarkIslands(grid,line,column-1)
        if line+1<len(grid) and grid[line+1][column]=='1':
            self.remarkIslands(grid,line+1,column)
        if column+1<len(grid[0]) and grid[line][column+1]=='1':
            self.remarkIslands(grid,line,column+1)
