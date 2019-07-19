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
