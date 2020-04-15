class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        rep=0
        tmp=[]
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]==2:
                    tmp.append([row,column])
        rep=self.refillgrid(grid,tmp)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]==1:
                    return -1
        return rep
        
    def refillgrid(self,grid,nums):
        rep=0
        tmp=[]
        for num in nums:
            row=num[0]
            column=num[1]
            grid[row][column]='X'
            if row-1>=0 and grid[row-1][column]==1:
                grid[row-1][column]='X'
                tmp.append([row-1,column])
            if column-1>=0 and grid[row][column-1]==1:
                grid[row][column-1]='X'
                tmp.append([row,column-1])
            if row+1<len(grid) and grid[row+1][column]==1:
                grid[row+1][column]='X'
                tmp.append([row+1,column])
            if column+1<len(grid[0]) and grid[row][column+1]==1:
                grid[row][column+1]='X'
                tmp.append([row,column+1])
                
        if tmp:
            rep=1+self.refillgrid(grid,tmp)
        return rep
