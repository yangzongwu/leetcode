class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,len(grid[0])):
            grid[0][i]+=grid[0][i-1]
        for row in range(1,len(grid)):
            for column in range(1,len(grid[0])):
                grid[row][column]+=min(grid[row-1][column],grid[row][column-1])
        return grid[-1][-1]
