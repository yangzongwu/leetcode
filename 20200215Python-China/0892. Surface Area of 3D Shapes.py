'''
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

'''
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        cnt=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    cnt+=self.countSurfacePoint(grid,row,col)
        return cnt

    def countSurfacePoint(self,grid,row,col):
        rep=grid[row][col]*4+2
        if row-1>=0 and grid[row-1][col]>0:
            rep-=min(grid[row][col],grid[row-1][col])
        if col-1>=0 and grid[row][col-1]>0:
            rep-=min(grid[row][col],grid[row][col-1])
        if row+1<len(grid) and grid[row+1][col]>0:
            rep-=min(grid[row][col],grid[row+1][col])
        if col+1<len(grid[0]) and grid[row][col+1]>0:
            rep-=min(grid[row][col],grid[row][col+1])
        return rep
        
