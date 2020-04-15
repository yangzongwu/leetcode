'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(1,len(grid)):
            grid[row][0]=grid[row-1][0]+grid[row][0]
        for column in range(1,len(grid[0])):
            grid[0][column]=grid[0][column-1]+grid[0][column]
        for row in range(1,len(grid)):
            for column in range(1,len(grid[0])):
                grid[row][column]+=min(grid[row-1][column],grid[row][column-1])
        return grid[-1][-1]
