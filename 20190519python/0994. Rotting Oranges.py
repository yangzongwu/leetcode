class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rep=[]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    rep.append([row,col])
        cnt=self.getOrangesRotting(rep,grid)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    return -1
        return cnt
    
    def getOrangesRotting(self,rep,grid):
        if not rep:
            return 0
        tmp=[]
        for cur in rep:
            row,col=cur[0],cur[1]
            if row-1>=0 and grid[row-1][col]==1:
                grid[row-1][col]=2
                tmp.append([row-1,col])
            if col-1>=0 and grid[row][col-1]==1:
                grid[row][col-1]=2
                tmp.append([row,col-1])
            if row+1<len(grid) and grid[row+1][col]==1:
                grid[row+1][col]=2
                tmp.append([row+1,col])
            if col+1<len(grid[0]) and grid[row][col+1]==1:
                grid[row][col+1]=2
                tmp.append([row,col+1])
        if tmp:
            return 1+self.getOrangesRotting(tmp,grid)
        else:
            return 0
