'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col]==1:
                    obstacleGrid[row][col]='X'
        
        obstacleGrid[0][0]=1
        for row in range(1,len(obstacleGrid)):
            if obstacleGrid[row][0]!='X':
                obstacleGrid[row][0]=1
            else:
                for r in range(row,len(obstacleGrid)):
                    obstacleGrid[r][0]='X'

        for col in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][col]!='X':
                obstacleGrid[0][col]=1
            else:
                for c in range(col,len(obstacleGrid[0])):
                    obstacleGrid[0][c]='X'

        for row in range(1,len(obstacleGrid)):
            for col in range(1,len(obstacleGrid[0])):
                if obstacleGrid[row][col]=='X':
                    continue
                if obstacleGrid[row-1][col]=='X' and obstacleGrid[row][col-1]=='X':
                    obstacleGrid[row][col]='X'
                else:
                    rep=0
                    if obstacleGrid[row-1][col]!='X':
                        rep+=obstacleGrid[row-1][col]
                    if obstacleGrid[row][col-1]!='X':
                        rep+=obstacleGrid[row][col-1]
                    obstacleGrid[row][col]=rep
        
        if obstacleGrid[-1][-1]=='X':
            return 0
        return obstacleGrid[-1][-1]
