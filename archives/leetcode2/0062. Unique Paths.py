class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        arraymn=[[1 for _ in range(m)] for _ in range(n)]
        for row in range(1,n):
            for column in range(1,m):
                arraymn[row][column]=arraymn[row-1][column]+arraymn[row][column-1]
        return arraymn[-1][-1]
        
        
