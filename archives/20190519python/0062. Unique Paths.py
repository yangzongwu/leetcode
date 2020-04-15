class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[([1]*m) for j in range(n)]
        for row in range(1,n):
            for col in range(1,m):
                grid[row][col]=grid[row-1][col]+grid[row][col-1]
        return grid[-1][-1]
