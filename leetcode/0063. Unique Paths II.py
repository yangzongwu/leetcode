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
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:return 0
        if obstacleGrid[-1][-1]==1:return 0
        if obstacleGrid[0][0]==1:return 0
        for row in range(len(obstacleGrid)):
            for column in range(len(obstacleGrid[0])):
                if obstacleGrid[row][column]==1:
                    obstacleGrid[row][column]='X'
     
        for row in range(len(obstacleGrid)):
            if obstacleGrid[row][0]!='X':
                obstacleGrid[row][0]=1
            else:
                for row in range(row,len(obstacleGrid)):
                    obstacleGrid[row][0]='X'
                break
                
        for column in range(len(obstacleGrid[0])):
            if obstacleGrid[0][column]!='X':
                obstacleGrid[0][column]=1
            else:
                for column in range(column,len(obstacleGrid[0])):
                    obstacleGrid[0][column]='X'
                break
                
        for row in range(1,len(obstacleGrid)):
            for column in range(1,len(obstacleGrid[0])):
                if obstacleGrid[row][column]!='X':
                    if obstacleGrid[row][column-1]=='X' and  obstacleGrid[row-1][column]=='X':
                        obstacleGrid[row][column]=0
                    elif obstacleGrid[row][column-1]!='X' and  obstacleGrid[row-1][column]=='X':
                        obstacleGrid[row][column]=obstacleGrid[row][column-1]
                    elif obstacleGrid[row][column-1]=='X' and  obstacleGrid[row-1][column]!='X':
                        obstacleGrid[row][column]=obstacleGrid[row-1][column]
                    else:
                        obstacleGrid[row][column]=obstacleGrid[row][column-1]+obstacleGrid[row-1][column]
        return obstacleGrid[-1][-1]
