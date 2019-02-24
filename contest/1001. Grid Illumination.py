class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        nums=self.buildnums(N,lamps)
        
        rep=[]
        for query in queries:
            if nums[query[0]][query[1]]==1:
                nums[query[0]][query[1]]=0
                rep.append(1)
            else:
                rep.append(0)
            nums=self.querynums(N,query[0],query[1],nums,lamps)
        return rep
    
    
    
    def querynums(self,N,row,column,nums,lamps):
        if row-1>=0 and nums[row-1][column]==1:
            if [row-1,column] in lamps:
                lamps.remove([row-1,column])
        if row+1<len(nums) and nums[row+1][column]==1:
            if [row+1,column] in lamps:
                lamps.remove([row+1,column])
        if column-1>=0 and nums[row][column-1]==1:
            if [row,column-1] in lamps:
                lamps.remove([row,column-1])
        if column+1<len(nums[0])and nums[row][column+1]==1:
            if [row,column+1] in lamps:
                lamps.remove([row,column+1])
        if row-1>=0 and column-1>=0 and nums[row-1][column-1]==1:
            if [row-1,column-1] in lamps:
                lamps.remove([row-1,column-1])
        if row-1>=0 and column+1<len(nums[0]) and nums[row-1][column+1]==1:
            if [row-1,column+1] in lamps:
                lamps.remove([row-1,column+1])
        if row+1<len(nums) and column-1>=0 and nums[row+1][column-1]==1:
            if [row+1,column-1] in lamps:
                lamps.remove([row+1,column-1])
        if row+1<len(nums) and column+1<len(nums[0]) and nums[row+1][column+1]==1:
            if [row+1,column+1] in lamps:
                lamps.remove([row+1,column+1])
        
        nums=self.buildnums(N,lamps)
        return nums
        
    def buildnums(self,N,lamps):
        nums=[[0 for _ in range(N)] for _ in range(N)]    
        for lamp in lamps:
            self.fillnums(lamp[0],lamp[1],nums)
        return nums    
        
    
    def fillnums(self,i,j,nums):
        row,column=i,j
        nums[row][column]=1
        
        row,column=i,j
        while row-1>=0:
            nums[row-1][column]=1
            row-=1
        
        row,column=i,j
        while column-1>=0:
            nums[row][column-1]=1
            column-=1
        
        row,column=i,j
        while row+1<len(nums):
            nums[row+1][column]=1
            row+=1 
        
        row,column=i,j
        while column+1<len(nums[0]):
            nums[row][column+1]=1
            column+=1
        
        row,column=i,j
        while row-1>=0 and column-1>=0:
            nums[row-1][column-1]=1
            row-=1
            column-=1
        
        row,column=i,j
        while row+1<len(nums) and column+1<len(nums[0]):
            nums[row+1][column+1]=1
            row+=1
            column+=1

        row,column=i,j
        while row-1>=0 and column+1<len(nums[0]):
            nums[row-1][column+1]=1
            row-=1
            column+=1
        
        row,column=i,j
        while row+1<len(nums) and column-1>=0:
            nums[row+1][column-1]=1
            row+=1
            column-=1
        
