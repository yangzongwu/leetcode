class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rep=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]!=0:
                    rep=max(rep,self.getrcMaximumGold(row,col,grid))
        return rep
    
    def getrcMaximumGold(self,row,col,grid):
        if grid[row][col]==0:
            return 0
        if grid[row][col]=='X':
            return 0
        rep=grid[row][col]
        grid[row][col]='X'
        cur=0
        if row-1>=0:
            cur=max(self.getrcMaximumGold(row-1,col,grid),cur)
        if col-1>=0:
            cur=max(self.getrcMaximumGold(row,col-1,grid),cur)
        if row+1<len(grid):
            cur=max(self.getrcMaximumGold(row+1,col,grid),cur)
        if col+1<len(grid[0]):
            cur=max(self.getrcMaximumGold(row,col+1,grid),cur)
        grid[row][col]=rep
        return rep+cur
