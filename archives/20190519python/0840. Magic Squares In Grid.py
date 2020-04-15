class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                if self.isMagicSq(row,col,grid):
                    cnt+=1
        return cnt
    
    def isMagicSq(self,row,col,grid):
        totalNum=set()
        for i in range(0,3):
            for j in range(0,3):
                if grid[row+i][col+j]>9 or grid[row+i][col+j]==0:
                    return False
                totalNum.add(grid[row+i][col+j])
        if len(totalNum)!=9:
            return False
        target=grid[row][col]+grid[row][col+1]+grid[row][col+2]
        for r in range(row,row+3):
            rowSum=0
            for c in range(col,col+3):
                rowSum+=grid[r][c]
            if rowSum!=target:
                return False
        
        for c in range(col,col+3):
            colSum=0
            for r in range(row,row+3):
                colSum+=grid[r][c]
            if colSum!=target:
                return False
            
        if grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]!=target:
            return False
        if grid[row+2][col]+grid[row+1][col+1]+grid[row][col+2]!=target:
            return False
        return True
