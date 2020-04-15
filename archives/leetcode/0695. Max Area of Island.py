'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rep=0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]==1:
                    tmp=self.submaxAreaOfIsland(row,column,grid)
                    rep=max(rep,tmp)
        return rep
    
    def submaxAreaOfIsland(self,row,column,grid):
        grid[row][column]='X'
        rep=1
        if row-1>=0 and grid[row-1][column]==1:
            rep+=self.submaxAreaOfIsland(row-1,column,grid)
        if column-1>=0 and grid[row][column-1]==1:
            rep+=self.submaxAreaOfIsland(row,column-1,grid)
        if row+1<len(grid) and grid[row+1][column]==1:
            rep+=self.submaxAreaOfIsland(row+1,column,grid)
        if column+1<len(grid[0]) and grid[row][column+1]==1:
            rep+=self.submaxAreaOfIsland(row,column+1,grid)
        return rep
