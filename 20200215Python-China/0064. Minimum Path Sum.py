'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

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
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(1,len(grid)):
            grid[row][0]+=grid[row-1][0]
        for col in range(1,len(grid[0])):
            grid[0][col]+=grid[0][col-1]

        for row in range(1,len(grid)):
            for col in range(1,len(grid[0])):
                grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
        
        return grid[-1][-1]
