'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return self.countPerimeter(grid,row,col)
        return 0

    def countPerimeter(self,grid,row,col):
        grid[row][col]=2
        cnt=4
        if row-1>=0:
            if grid[row-1][col]==1:
                cnt+=self.countPerimeter(grid,row-1,col)-1
            elif grid[row-1][col]==2:
                cnt-=1
        if col-1>=0:
            if grid[row][col-1]==1:
                cnt+=self.countPerimeter(grid,row,col-1)-1
            elif grid[row][col-1]==2:
                cnt-=1 
        if row+1<len(grid):
            if grid[row+1][col]==1:
                cnt+=self.countPerimeter(grid,row+1,col)-1
            elif grid[row+1][col]==2:
                cnt-=1
        if col+1<len(grid[0]):
            if grid[row][col+1]==1:
                cnt+=self.countPerimeter(grid,row,col+1)-1
            elif grid[row][col+1]==2:
                cnt-=1
        return cnt
